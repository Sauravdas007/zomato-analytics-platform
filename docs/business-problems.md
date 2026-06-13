# Business Problems Solved

## Overview
This project was designed as an end-to-end **Food Delivery Analytics Platform** built on Azure Synapse Analytics. The goal was not simply to visualize data, but to solve real business problems faced by food delivery platforms such as **Zomato, Swiggy, Uber Eats, and DoorDash**.

The platform addresses six major analytics domains.

---

# 1. Revenue Growth Optimization

## Business Question
How can the platform increase revenue by understanding customer spending patterns and restaurant performance?

## Challenges
- Revenue sources vary across cities and cuisines.  
- High-performing restaurants need to be identified.  
- Seasonal revenue trends are difficult to detect from raw transactional data.  

## Solution
Built revenue-focused Gold marts that aggregate:
- Monthly revenue  
- Revenue by city  
- Revenue by cuisine  
- Top revenue-generating restaurants  

## Outputs
- Monthly revenue trends  
- Top-performing cities  
- Cuisine contribution analysis  
- Revenue concentration insights  
- Average order value  

## Business Value
Enables leadership to identify revenue drivers and allocate resources toward profitable regions and restaurant partnerships.

---

# 2. Customer Segmentation

## Business Question
Can customers be grouped into meaningful segments for targeted marketing campaigns?

## Challenges
Customers exhibit different purchasing behaviors based on:
- Age  
- Occupation  
- Income  
- Spending patterns  
- Ordering frequency  

## Solution
Built customer segmentation marts using:
- Demographics  
- Income brackets  
- Spending behavior  
- Order activity  

## Segments
- **Premium Customers**: High-spending customers with strong purchasing power.  
- **Budget Customers**: Price-sensitive users focused on affordability.  
- **Frequent Buyers**: Customers placing orders regularly.  
- **Occasional Buyers**: Users with low ordering frequency.  

## Business Value
Supports personalized marketing, promotions, and customer acquisition strategies.

---

# 3. Customer Retention Analytics

## Business Question
Which customers are highly loyal and which customers are at risk of churn?

## Challenges
Revenue growth is heavily dependent on customer retention.  
Organizations need to identify:
- Active users  
- Dormant users  
- High-value customers  

## Solution
Implemented **RFM Analysis**:
- **Recency**: How recently a customer placed an order.  
- **Frequency**: How often a customer places orders.  
- **Monetary**: Total customer spending.  

## Outputs
- Loyal Customers  
- At-Risk Customers  
- Active Customers  
- Dormant Customers  

## Business Value
Allows proactive retention campaigns and loyalty program optimization.

---

# 4. Restaurant Performance Intelligence

## Business Question
Which restaurant partners create the highest value for the platform?

## Challenges
Thousands of restaurants contribute differently to:
- Revenue  
- Customer engagement  
- Ratings  
- Order volume  

## Solution
Created restaurant intelligence marts analyzing:
- Revenue  
- Orders  
- Ratings  
- Rating counts  
- Cost ranges  

## Outputs
- Top-performing restaurants  
- Underperforming restaurants  
- City-wise restaurant analysis  
- Restaurant rankings  

## Business Value
Supports restaurant onboarding, partnership decisions, and growth strategies.

---

# 5. Demand & Revenue Forecasting

## Business Question
What will future order demand and revenue look like?

## Challenges
Food delivery demand fluctuates due to:
- Seasonality  
- Customer behavior  
- Regional demand patterns  

## Solution
Created forecasting datasets using:
- Historical order volume  
- Historical revenue  
- Monthly demand trends  

## Outputs
- Revenue forecasts  
- Order forecasts  
- Trend analysis  
- Seasonal insights  

## Business Value
Supports planning, budgeting, staffing, and operational decision-making.

---

# 6. Executive Analytics Platform

## Business Question
How can leadership obtain a unified view of platform performance?

## Solution
Designed a centralized **Power BI Executive Dashboard** integrating:
- Revenue Analytics  
- Customer Analytics  
- Restaurant Intelligence  
- Retention Analytics  
- Forecasting Analytics  

## Dashboard Features
- KPI Monitoring  
- Interactive Filtering  
- Drill-Down Analysis  
- Geographic Insights  
- Forecasting Insights  

## Business Value
Provides executives with a single source of truth for strategic decision-making.

---

# Summary
The project transforms raw food delivery data into **actionable business intelligence** through a scalable **Medallion Architecture** built on **Azure Synapse Analytics** and **Power BI**.
