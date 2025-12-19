📊 Cohort-Based Retention & Churn Analysis for SaaS
📌 Project Overview

This project is an end-to-end data analysis portfolio project focused on customer retention, churn, and customer lifetime value (LTV) for a SaaS (Software-as-a-Service) business. The purpose of this project is to demonstrate practical data analyst skills using SQL, Python, and Power BI, along with clear business thinking and storytelling. All data used in this project is synthetic (mock data) but designed to closely represent real-world SaaS subscription behavior.

🎯 Business Questions Answered

Which customer cohorts generate the highest lifetime value (LTV)?

When do most customers churn (early months vs later months)?

How does retention change by cohort month?

How does retention differ by pricing tier (Basic, Pro, Enterprise)?

Which acquisition channels bring higher-quality customers?

Which customers are currently at high churn risk?

🧱 Data Used (Synthetic SaaS Data)

All datasets were generated using Python to simulate a monthly subscription-based SaaS model.

Files used in this project:

cohort_customers.csv – Customer details including cohort month, pricing tier, and acquisition channel

cohort_orders.csv – Monthly recurring subscription order data

Data summary:

5,000 customers

Cohorts from January 2023 to June 2024

Monthly recurring revenue model

Tier-based pricing structure

⚙️ Data Generation

Python was used to generate realistic mock data, including cohort assignment, pricing tiers, acquisition channels, monthly billing, and churn probability logic. This ensures the data behaves similarly to real SaaS data while remaining safe for public sharing.

🔍 Analysis Performed

Cohort Retention Analysis:
Customers were grouped by signup month, and retention was tracked month-by-month to understand how long users stay active after signup.

Lifetime Value (LTV) by Cohort:
Customer revenue was aggregated to calculate average lifetime value for each cohort, allowing comparison of long-term value across signup periods.

Retention by Pricing Tier:
Retention curves were created for Basic, Pro, and Enterprise plans to understand how pricing impacts customer longevity.

Churn Risk Segmentation:
Customers were classified into Low, Medium, High, and Critical churn risk groups based on days since last activity.

🐍 Python Dashboards & Visualizations

Python was used to create dashboard-style visualizations for analysis and insight validation.

Visualization files:

cohort_retention_heatmap.png – Cohort-based monthly retention heatmap

ltv_by_cohort.png – Dashboard-style visualization showing average LTV by cohort

retention_by_tier.png – Dashboard-style visualization comparing retention by pricing tier

churn_risk.png – Dashboard-style visualization showing churn risk distribution

Transparency note:
The Python visualization code used to generate these charts was created with the assistance of Claude (Anthropic AI). The analysis logic, metric definitions, validation of results, interpretation of insights, Power BI dashboard creation, and all documentation were done by me.

📊 Power BI Dashboard (Final Deliverable)

File: cohort_retention_dashboard.pbix

The final interactive dashboard was built in Power BI and represents the main deliverable of this project. It combines all insights into an executive-friendly format.

Dashboard includes:

Cohort retention heatmap

LTV trends by cohort

Retention comparison by pricing tier

Churn risk segmentation

Month-over-month retention analysis

Power BI Dashboard Screenshots (to be added):

[INSERT POWER BI DASHBOARD OVERVIEW SCREENSHOT]

[INSERT POWER BI COHORT RETENTION SCREENSHOT]

[INSERT POWER BI LTV & CHURN SCREENSHOT]

🗄 SQL Analysis

SQL was used through a single SQL file to perform cohort creation, retention calculation, LTV analysis, churn measurement by pricing tier, and acquisition channel performance analysis. The SQL includes joins, aggregations, date calculations, and common table expressions (CTEs).

📌 Key Insights

Enterprise-tier customers have the highest retention and lifetime value

Most customer churn happens within the first 60 days

Referral and Organic acquisition channels produce higher-quality customers

Small improvements in early retention can lead to significant revenue growth

Example: Improving Month-2 retention by just 5% can significantly increase total customer lifetime value.

🚀 Future Improvements

Add a churn prediction model

Track feature usage to identify “aha moments”

Simulate A/B tests for onboarding and pricing

Forecast revenue impact of retention improvements

