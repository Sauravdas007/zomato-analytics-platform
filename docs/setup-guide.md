# 🚀 Setup Guide

This guide walks through the complete setup process for building and running the Zomato Analytics Platform using Azure Synapse Analytics, Azure Data Lake Storage Gen2, Apache Spark, and Power BI Desktop.

The setup is designed for:

- Students using Azure Student Credits
- Beginners learning Data Engineering
- Portfolio Projects
- Low-Cost Cloud Usage

---

# 📋 Prerequisites

Before starting, ensure you have:

- Microsoft Account
- Azure Student Account
- GitHub Account
- Power BI Desktop
- Basic Python Knowledge
- Basic SQL Knowledge

---

# 🎓 Azure Student Subscription

## Why Azure Student?

Azure Student provides:

- Free Azure Credits
- No Credit Card Required
- Access to Azure Synapse Analytics
- Access to Azure Data Lake Storage Gen2

Perfect for portfolio projects and learning cloud analytics.

---

## Create Student Subscription

Visit:

https://azure.microsoft.com/free/students/

Sign in with:

- College Email
- University Email

Verify your student status.

Once approved, Azure credits will be added automatically.

---

# 🏗️ Resource Architecture

```text
Azure Subscription
│
├── Resource Group
│
├── Azure Data Lake Storage Gen2
│
└── Azure Synapse Analytics
      │
      ├── Spark Pool
      ├── Workspace
      └── Data Lake Integration
```

---

# 📂 Create Resource Group

Navigate to:

Azure Portal
→ Resource Groups
→ Create

Example:

```text
rg-zomato-analytics
```

Region:

```text
Central India
```

---

# 💾 Create Azure Data Lake Storage Gen2

Navigate to:

Azure Portal
→ Storage Accounts
→ Create

Recommended Settings:

| Setting | Value |
|----------|--------|
| Performance | Standard |
| Redundancy | LRS |
| Hierarchical Namespace | Enabled |

Example Name:

```text
stzomatoanalytics01
```

---

# 📁 Create Containers

Inside ADLS Gen2 create:

```text
bronze
silver
gold
```

---

# 🧠 Create Azure Synapse Workspace

Navigate to:

Azure Portal
→ Synapse Analytics
→ Create

Recommended Settings:

| Setting | Value |
|----------|--------|
| Managed Resource Group | Auto |
| Storage Account | Existing ADLS |
| File System | bronze |

---

# ⚡ Create Spark Pool

Navigate:

Synapse Studio
→ Manage
→ Apache Spark Pools
→ New

Recommended Student Settings:

| Setting | Value |
|----------|--------|
| Node Size | Small |
| Autoscale | Enabled |
| Min Nodes | 3 |
| Max Nodes | 3 |
| Auto Pause | 15 Minutes |

---

# 💰 Cost Optimization

For Student Credits:

Always use:

```text
Small Spark Pool
3 Nodes
Auto Pause = 15 Minutes
```

Avoid:

❌ Dedicated SQL Pools

❌ Large Spark Pools

❌ Long Running Sessions

Dedicated SQL Pools can consume credits very quickly.

For this project:

✅ Serverless Architecture

✅ Spark Only Processing

is sufficient.

---

# 📥 Upload Dataset

Download dataset from Kaggle.

Upload files into:

```text
bronze/
├── users.csv
├── restaurants.csv
├── orders.csv
├── food.csv
└── menu.csv
```

Using:

Synapse Studio
→ Data
→ Linked Storage
→ Upload

---

# 🔄 Data Engineering Workflow

## Bronze Layer

Store raw files exactly as received.

```text
CSV Files
```

No transformations.

---

## Silver Layer

Perform:

- Schema Validation
- Data Cleaning
- Type Casting
- Duplicate Removal
- Null Handling

Output:

```text
Parquet
```

---

## Gold Layer

Create business marts:

```text
revenue_monthly
revenue_city
revenue_cuisine
customer_segments
rfm_customers
restaurant_intelligence
top_restaurants
forecast_base
revenue_forecast
executive_kpis
```

Output:

```text
Parquet
```

---

# 📊 Install Power BI Desktop

Download:

https://powerbi.microsoft.com/desktop/

Install:

```text
Power BI Desktop
```

Free version is sufficient.

No Power BI Service subscription is required.

---

# 🔗 Connect Power BI to ADLS Gen2

Open Power BI Desktop

Navigate:

```text
Get Data
→ Azure
→ Azure Data Lake Storage Gen2
```

Sign in using the same Azure account.

Use:

```text
File System View
```

Browse:

```text
gold/
```

Load required Gold datasets.

---

# 📈 Build Dashboard

Recommended Pages:

## Executive Overview

KPIs:

- Revenue
- Orders
- Customers
- Restaurants

---

## Revenue Analytics

Visuals:

- Revenue Trend
- Revenue by City
- Revenue by Cuisine

---

## Customer Analytics

Visuals:

- Customer Segments
- RFM Analysis
- Retention Metrics

---

## Restaurant Analytics

Visuals:

- Top Restaurants
- Restaurant Revenue
- Restaurant Ratings

---

## Forecasting

Visuals:

- Revenue Forecast
- Monthly Forecast
- Growth Trend

---

# 🔒 Shut Down Resources

To avoid consuming Azure credits:

After every session:

### Stop Spark Pool

Synapse Studio
→ Monitor
→ Running Sessions
→ Stop Session

### Wait for Auto Pause

Spark pool pauses automatically.

### Verify

Azure Portal
→ Synapse Workspace
→ Spark Pools

Status:

```text
Stopped
```

---

# 🎯 Estimated Cost

With Student Credits:

| Service | Cost |
|----------|--------|
| ADLS Gen2 | Very Low |
| Synapse Workspace | Minimal |
| Small Spark Pool | Low |
| Power BI Desktop | Free |

Typical student project cost:

```text
<$10 worth of Azure credits
```

for development and testing.

---

# 📚 Learning Outcomes

By completing this project you will learn:

- Azure Data Lake Storage Gen2
- Azure Synapse Analytics
- Apache Spark
- PySpark
- Medallion Architecture
- Data Warehousing
- Star Schema Modeling
- Power BI
- Revenue Analytics
- Customer Segmentation
- RFM Analytics
- Forecasting Pipelines
- Executive Dashboard Development

---

# 🏆 Portfolio Value

This project demonstrates:

- Cloud Data Engineering
- Analytics Engineering
- Data Warehousing
- Business Intelligence
- End-to-End Azure Analytics Platform Design

Suitable for:

- Data Engineer Roles
- Analytics Engineer Roles
- Business Intelligence Roles
- Azure Data Engineer Portfolio Projects