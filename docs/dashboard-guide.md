# Dashboard Guide

## Overview
The **Executive Analytics Dashboard** serves as the presentation layer of the platform and provides decision-makers with actionable business insights derived from the Gold analytical marts.

The dashboard consists of **five major analytics pages**.

---

# Page 1 — Executive Overview

## Purpose
Provides a high-level snapshot of platform performance.

## KPIs
- Total Revenue  
- Total Orders  
- Total Customers  
- Average Order Value  
- Active Customers  

## Visualizations
- Revenue Trend  
- Top Cities  
- Top Restaurants  
- Revenue by Cuisine  
- Geographic Distribution  

## Business Outcome
Allows executives to quickly assess overall business health.

---

# Page 2 — Revenue Intelligence

## Purpose
Analyze revenue generation across multiple dimensions.

## KPIs
- Total Revenue  
- Monthly Growth %  
- Average Order Value  
- Top Revenue City  

## Visualizations
- **Monthly Revenue Trend** → Tracks revenue growth over time.  
- **Revenue by City** → Identifies strongest geographic markets.  
- **Revenue by Cuisine** → Determines cuisine profitability.  
- **Top Restaurants by Revenue** → Highlights major revenue contributors.  

## Business Outcome
Supports revenue optimization strategies.

---

# Page 3 — Customer Intelligence

## Purpose
Understand customer behavior and segmentation.

## KPIs
- Total Customers  
- Premium Customers  
- Frequent Buyers  
- Loyal Customers  

## Visualizations
- **Customer Segment Distribution** → Breakdown of customer groups.  
- **Income vs Spending** → Relationship between purchasing power and spending.  
- **Occupation Analysis** → Customer demographics by occupation.  
- **RFM Distribution** → Retention-focused customer segmentation.  

## Business Outcome
Supports targeted marketing initiatives.

---

# Page 4 — Restaurant Intelligence

## Purpose
Evaluate restaurant partner performance.

## KPIs
- Total Restaurants  
- Average Rating  
- Highest Rated Restaurant  
- Top Revenue Restaurant  

## Visualizations
- **Top Restaurants** → Revenue and rating rankings.  
- **Rating vs Revenue** → Performance relationship analysis.  
- **Geographic Performance** → Restaurant contribution by city.  
- **Performance Categories** → Top Performers, Average Performers, and Underperformers.  

## Business Outcome
Supports partnership and marketplace decisions.

---

# Page 5 — Forecasting Analytics

## Purpose
Provide visibility into future demand and revenue.

## KPIs
- Forecast Revenue  
- Forecast Orders  
- Growth Projection  

## Visualizations
- **Actual vs Forecast Revenue** → Comparison of historical and projected values.  
- **Monthly Forecast Trend** → Projected revenue trajectory.  
- **Seasonal Analysis** → Recurring demand patterns.  

## Business Outcome
Supports operational planning and strategic forecasting.

---

# Dashboard Features

## Interactive Filters
Users can filter by:
- City  
- Cuisine  
- Customer Segment  
- Date  
- Restaurant  

## Cross-Filtering
All visualizations interact dynamically to provide deeper analysis.

## Drill-Down Capabilities
Users can navigate from executive KPIs into detailed analytical views.

---

# Data Sources

The dashboard is powered by **Gold-layer analytical marts** generated in Azure Synapse Analytics.

## Gold Datasets
- executive_kpis  
- revenue_monthly  
- revenue_city  
- revenue_cuisine  
- customer_segments  
- rfm_customers  
- restaurant_intelligence  
- top_restaurants  
- revenue_forecast  
- monthly_forecast  
- forecast_base  

---

# Technology Stack
- Azure Data Lake Storage Gen2  
- Azure Synapse Analytics  
- Apache Spark (PySpark)  
- Parquet  
- Power BI Desktop  

---

# Outcome
The dashboard transforms raw transactional food delivery data into **executive-level insights** covering revenue, customer behavior, restaurant performance, retention analytics, and forecasting.
