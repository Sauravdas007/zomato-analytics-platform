# Solution Architecture: Food Delivery Analytics Platform
> **Project:** Zomato Data Analytics  
> **Last Updated:** June 2026  
> **Status:** Design Phase

---

## 1. Business Objective

Build a **Food Delivery Analytics Platform** that enables:

| # | Objective | Description |
|---|-----------|-------------|
| 1 | **Revenue Growth Analytics** | Track and analyse revenue trends across time, cities, cuisines, and restaurants |
| 2 | **Customer Segmentation** | Group customers by demographics, income, occupation, and behaviour |
| 3 | **Customer Retention Analysis (RFM)** | Score customers on Recency, Frequency, and Monetary value |
| 4 | **Restaurant Performance Intelligence** | Rank and benchmark restaurants by revenue, orders, and ratings |
| 5 | **Demand & Revenue Forecasting** | Predict future orders and revenue using historical trends |
| 6 | **Executive Dashboard Reporting** | Deliver KPI summaries for leadership and stakeholders |

---

## 2. Source Data Overview

Based on profiling of the raw data:

| Table | Rows | Key Columns | Notes |
|-------|------|-------------|-------|
| `users.csv` | 100,000 | user_id, age, gender, occupation, monthly_income | No missing values |
| `orders.csv` | 150,281 | order_date, sales_qty, sales_amount, user_id, r_id | 1,617 missing r_id |
| `restaurants.csv` | 148,541 | id, name, city, rating, cost, cuisine | Minor nulls in name, rating, cost |
| `menu.csv` | 1,179,936 | menu_id, r_id, f_id, cuisine, price | Mixed dtype on price column |
| `food.csv` | 371,561 | f_id, item, veg_or_non_veg | 1 missing item/veg flag |

**Order date range:** 4 Oct 2017 → 26 Jun 2020 (~2.7 years)

---

## 3. Star Schema Design

Orders is the central fact — all analytical questions revolve around what was ordered, by whom, at which restaurant, and when.

Each dimension carries a **surrogate key** (system-generated integer PK) alongside the natural/business key from the source. The fact table references only surrogate keys — this insulates the warehouse from upstream ID changes and enables consistent handling of slowly changing dimensions.

```
                          dim_date
                         (date_key PK,
                          date BK,
                          day, month,
                         quarter, year,
                           weekday)
                              |
                              |
          dim_users ----  fact_orders  ---- dim_restaurants
        (user_key PK,    (order_id PK,    (restaurant_key PK,
         user_id BK,      date_key FK,     restaurant_id BK,
          age,            user_key FK,      name,
          gender,         restaurant_key    city,
          marital_status,   FK,             rating,
          occupation,     sales_qty,        rating_count,
          monthly_income, sales_amount,     cost,
          education,      currency)         cuisine)
          family_size)
```

> **BK = Business Key** (source system identifier, kept for traceability)  
> **PK = Surrogate Key** (warehouse-generated, used for all joins)

---

### 3.1 Fact Table — `fact_orders`

| Column | Source | Type | Notes |
|--------|--------|------|-------|
| `order_id` | orders.Unnamed: 0 | INT (PK) | Surrogate key |
| `date_key` | orders.order_date → dim_date | INT (FK) | → dim_date.date_key |
| `user_key` | orders.user_id → dim_users | INT (FK) | → dim_users.user_key |
| `restaurant_key` | orders.r_id → dim_restaurants | INT (FK) | → dim_restaurants.restaurant_key |
| `sales_qty` | orders.sales_qty | INT | Units ordered |
| `sales_amount` | orders.sales_amount | DECIMAL | Revenue value |
| `currency` | orders.currency | VARCHAR | Normalised to INR |

> **Note:** The fact table no longer stores raw `user_id`, `r_id`, or `order_date` directly — it joins via surrogate keys only. The business keys are preserved in the dimension tables for traceability and reverse-lookup.

---

### 3.2 Dimension 1 — `dim_users`

| Column | Source | Type | Notes |
|--------|--------|------|-------|
| `user_key` | Generated | INT (PK) | **Surrogate key** — warehouse-assigned |
| `user_id` | users.user_id | INT (BK) | **Business key** — source system ID |
| `age` | users.Age | INT | |
| `gender` | users.Gender | VARCHAR | |
| `marital_status` | users.Marital Status | VARCHAR | |
| `occupation` | users.Occupation | VARCHAR | |
| `monthly_income` | users.Monthly Income | VARCHAR | |
| `educational_qualification` | users.Educational Qualifications | VARCHAR | |
| `family_size` | users.Family size | INT | |

**Used for:** Customer segmentation, RFM analysis, demographic breakdowns

---

### 3.3 Dimension 2 — `dim_restaurants`

| Column | Source | Type | Notes |
|--------|--------|------|-------|
| `restaurant_key` | Generated | INT (PK) | **Surrogate key** — warehouse-assigned |
| `restaurant_id` | restaurants.id | INT (BK) | **Business key** — source system ID |
| `name` | restaurants.name | VARCHAR | |
| `city` | restaurants.city | VARCHAR | |
| `rating` | restaurants.rating | FLOAT | |
| `rating_count` | restaurants.rating_count | VARCHAR | |
| `cost` | restaurants.cost | VARCHAR | |
| `cuisine` | restaurants.cuisine | VARCHAR | |

**Used for:** Restaurant intelligence, revenue by city, revenue by cuisine

---

### 3.4 Dimension 3 — `dim_date`

*Derived from `order_date` in the orders table.*

| Column | Derivation | Type | Notes |
|--------|-----------|------|-------|
| `date_key` | Generated (YYYYMMDD int) | INT (PK) | **Surrogate key** — e.g. 20191025 |
| `date` | order_date | DATE (BK) | **Business key** — calendar date |
| `day` | day of month | INT | |
| `month` | month number | INT | |
| `month_name` | Jan–Dec | VARCHAR | |
| `quarter` | Q1–Q4 | INT | |
| `year` | year | INT | |
| `weekday` | Mon–Sun | VARCHAR | |
| `is_weekend` | Sat/Sun flag | BOOLEAN | |

> **Convention:** `date_key` uses YYYYMMDD integer format (e.g. `20191025`) — human-readable, sortable, and avoids date-type join mismatches across engines.

**Used for:** Time-series trends, seasonality, forecasting

---

## 4. Gold Business Marts

Aggregated tables built on top of the star schema for each analytical objective.

### 4.1 Revenue Mart — `gold_revenue`

| Metric | Grouping |
|--------|----------|
| Total Revenue | City, Restaurant, Cuisine, Month, Quarter, Year |
| Total Orders | City, Restaurant, Cuisine, Month |
| Average Order Value | Restaurant, Cuisine |
| Revenue Growth % | Month-over-Month, Year-over-Year |

---

### 4.2 Customer Mart — `gold_customers`

| Column | Description |
|--------|-------------|
| `user_id` | Customer business key |
| `total_spend` | Sum of all sales_amount |
| `order_count` | Total number of orders |
| `avg_order_value` | total_spend / order_count |
| `first_order_date` | Earliest order date |
| `last_order_date` | Most recent order date |
| `customer_lifetime_days` | last − first order date |

---

### 4.3 Retention Mart (RFM) — `gold_rfm`

| Column | Description |
|--------|-------------|
| `user_id` | Customer business key |
| `recency_days` | Days since last order |
| `frequency` | Total order count |
| `monetary` | Total spend |
| `r_score` | Recency score (1–5) |
| `f_score` | Frequency score (1–5) |
| `m_score` | Monetary score (1–5) |
| `rfm_score` | Combined RFM score |
| `segment` | Champion / Loyal / At Risk / Lost etc. |

---

### 4.4 Restaurant Mart — `gold_restaurants`

| Column | Description |
|--------|-------------|
| `restaurant_id` | Restaurant business key |
| `name` | Restaurant name |
| `city` | City |
| `cuisine` | Cuisine type |
| `total_revenue` | Sum of sales_amount |
| `total_orders` | Count of orders |
| `avg_revenue_per_order` | Revenue / Orders |
| `rating` | Restaurant rating |
| `revenue_rank_in_city` | Rank within city |

---

### 4.5 Forecast Mart — `gold_forecast`

| Column | Description |
|--------|-------------|
| `date` | Calendar date |
| `actual_revenue` | Observed revenue |
| `forecast_revenue` | Predicted revenue |
| `actual_orders` | Observed order count |
| `forecast_orders` | Predicted order count |
| `confidence_lower` | Forecast lower bound |
| `confidence_upper` | Forecast upper bound |

---

### 4.6 Segmentation Mart — `gold_segments`

*Output of the K-Means clustering pipeline. Each row represents one customer's cluster assignment, enriched with behavioural and demographic signals for BI consumption.*

| Column | Source | Description |
|--------|--------|-------------|
| `user_id` | dim_users.user_id | Customer business key |
| `cluster_id` | K-Means output | Numeric cluster label (0–N) |
| `segment_name` | Derived / labelled | Human-readable label (e.g. "High-Value Loyalist", "Occasional Budget Buyer") |
| `total_spend` | gold_customers | Sum of all orders — primary clustering feature |
| `order_count` | gold_customers | Order frequency — primary clustering feature |
| `avg_order_value` | gold_customers | Spend per order — primary clustering feature |
| `recency_days` | gold_rfm | Days since last order — primary clustering feature |
| `income_group` | dim_users.monthly_income | Binned income bracket (Low / Mid / High) |
| `occupation` | dim_users.occupation | Occupation category |
| `age_group` | dim_users.age | Binned age bracket (18–25, 26–35, 36–45, 45+) |

> **How this mart is built:**
> 1. Features are pulled from `gold_customers` (spend, frequency, AOV) and `gold_rfm` (recency) — all already aggregated.
> 2. K-Means is run on the normalised feature set. The cluster label is written back as `cluster_id`.
> 3. Cluster labels are named manually (or via centroid analysis) and stored as `segment_name`.
> 4. Demographic columns (`income_group`, `occupation`, `age_group`) are joined from `dim_users` to enrich the mart for BI slicing.
>
> **Feeds into:** Customer segmentation dashboard, targeted campaign lists, cohort-level revenue analysis.

---

## 5. Data Layer Architecture

```
RAW LAYER          SILVER LAYER               GOLD LAYER
(CSV files)    →   (Surrogate-keyed dims    →  (Business Marts)
                    & fact tables)

users.csv      →   dim_users                →  gold_rfm
               →   (user_key + user_id BK)  →  gold_customers
                                            →  gold_segments ← K-Means

orders.csv     →   fact_orders              →  gold_revenue
               →   (date_key, user_key,     →  gold_forecast
                    restaurant_key FKs)

restaurants    →   dim_restaurants          →  gold_restaurants
               →   (restaurant_key + id BK)

menu.csv       →   (supporting)
food.csv       →   (supporting)

date spine     →   dim_date
               →   (date_key + date BK)
```

---

## 6. Data Quality Issues to Resolve

| Issue | Table | Column | Action |
|-------|-------|--------|--------|
| 1,617 missing r_id | orders | r_id | Assign to a sentinel `restaurant_key = -1` ("Unknown Restaurant") in dim_restaurants; preserve orders in fact |
| Mixed dtypes on price | menu | price | Cast to FLOAT, coerce errors to NaN |
| 86 missing names/ratings | restaurants | name, rating | Exclude from restaurant mart |
| 1 missing item | food | item | Drop row |
| Duplicate menu_id | menu | menu_id | Investigate — 1.18M rows vs 1.05M unique |
| Currency contains whitespace artifacts (INR vs INR\r).
| Trim whitespace and standardize to INR.
| Two USD records identified and treated as anomalies.

> **Surrogate key note on missing r_id:** Rather than excluding orders with missing `r_id`, map them to a dedicated sentinel row in `dim_restaurants` (`restaurant_key = -1`, `name = "Unknown"`, all attributes NULL). This preserves revenue in the fact table and allows analysts to quantify unattributed spend — currently ~1% of orders.

---

## 7. Docs Folder Structure

```
docs/
├── data_profiling.md          ← profiling output summary
├── solution_architecture.md   ← this file
└── star_schema.png            ← optional visual export
```

---

## 8. Next Steps

- [ ] Build ETL pipeline: raw → silver (cleaned dims + fact with surrogate keys)
- [ ] Generate `dim_date` spine from full order date range
- [ ] Build gold mart aggregations (revenue, customers, RFM)
- [ ] Validate referential integrity post-load
- [ ] Build RFM scoring logic
- [ ] Run K-Means on `gold_customers` + `gold_rfm` features → write output to `gold_segments`
- [ ] Label clusters and populate `segment_name`
- [ ] Connect to BI tool (Power BI / Tableau / Streamlit)
- [ ] Build daily revenue forecasting model using Spark MLlib → `gold_forecast`
- [ ] Evaluate using RMSE and MAE
- [ ] Generate 30-day forecast horizon
