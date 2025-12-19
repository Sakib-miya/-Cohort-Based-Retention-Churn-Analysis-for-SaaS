import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
customers = pd.read_csv('cohort_customers.csv')
orders = pd.read_csv('cohort_orders.csv')

# Convert dates
orders['order_date'] = pd.to_datetime(orders['order_date'])
orders['cohort_month'] = pd.to_datetime(orders['cohort_month'])

# 1. COHORT RETENTION HEATMAP
cohort_pivot = orders.groupby(['cohort_month', 'month_number']).agg({
    'customer_id': 'nunique'
}).reset_index()

cohort_sizes = orders.groupby('cohort_month')['customer_id'].nunique()
cohort_pivot['cohort_size'] = cohort_pivot['cohort_month'].map(cohort_sizes)
cohort_pivot['retention_rate'] = cohort_pivot['customer_id'] / cohort_pivot['cohort_size'] * 100

retention_matrix = cohort_pivot.pivot(index='cohort_month', 
                                      columns='month_number', 
                                      values='retention_rate')

plt.figure(figsize=(14, 8))
sns.heatmap(retention_matrix, annot=True, fmt='.1f', cmap='RdYlGn', 
            cbar_kws={'label': 'Retention %'})
plt.title('Cohort Retention Analysis - % of Customers Active Each Month', fontsize=16)
plt.xlabel('Months Since Signup')
plt.ylabel('Cohort Month')
plt.tight_layout()
plt.savefig('cohort_retention_heatmap.png', dpi=300)
plt.show()

# 2. LTV BY COHORT
ltv_by_cohort = orders.groupby(['cohort_month', 'customer_id'])['revenue'].sum().reset_index()
ltv_avg = ltv_by_cohort.groupby('cohort_month')['revenue'].mean()

plt.figure(figsize=(12, 6))
ltv_avg.plot(kind='bar', color='steelblue')
plt.title('Average Customer Lifetime Value by Cohort', fontsize=14)
plt.xlabel('Cohort Month')
plt.ylabel('Average LTV ($)')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('ltv_by_cohort.png', dpi=300)
plt.show()

# 3. RETENTION CURVES BY TIER
for tier in ['Basic', 'Pro', 'Enterprise']:
    tier_data = orders[orders['tier'] == tier]
    retention = tier_data.groupby('month_number')['customer_id'].nunique()
    retention_pct = retention / retention.iloc[0] * 100
    plt.plot(retention_pct.index, retention_pct.values, marker='o', label=tier, linewidth=2)

plt.title('Retention Curves by Pricing Tier', fontsize=14)
plt.xlabel('Months Since Signup')
plt.ylabel('Retention Rate (%)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('retention_by_tier.png', dpi=300)
plt.show()

# 4. CHURN RISK SCORE
latest_date = orders['order_date'].max()
last_order = orders.groupby('customer_id')['order_date'].max().reset_index()
last_order['days_since_last_order'] = (latest_date - last_order['order_date']).dt.days

customers_with_churn = customers.merge(last_order, on='customer_id')
customers_with_churn['churn_risk'] = pd.cut(customers_with_churn['days_since_last_order'],
                                             bins=[0, 30, 60, 90, 999],
                                             labels=['Low', 'Medium', 'High', 'Critical'])

risk_counts = customers_with_churn['churn_risk'].value_counts()
plt.figure(figsize=(8, 6))
risk_counts.plot(kind='bar', color=['green', 'yellow', 'orange', 'red'])
plt.title('Customer Churn Risk Distribution', fontsize=14)
plt.xlabel('Risk Level')
plt.ylabel('Number of Customers')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('churn_risk.png', dpi=300)
plt.show()

print("✅ All visualizations saved!")