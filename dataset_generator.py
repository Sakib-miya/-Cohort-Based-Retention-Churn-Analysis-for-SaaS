import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

# Parameters
n_customers = 5000
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)

# Generate customers with cohort months
cohort_months = pd.date_range(start='2023-01', end='2024-06', freq='MS')
customers = []

for customer_id in range(1, n_customers + 1):
    cohort_month = random.choice(cohort_months)
    tier = random.choices(['Basic', 'Pro', 'Enterprise'], weights=[50, 35, 15])[0]
    channel = random.choices(['Organic', 'Paid', 'Referral', 'Social'], 
                            weights=[30, 40, 20, 10])[0]
    
    customers.append({
        'customer_id': customer_id,
        'cohort_month': cohort_month,
        'tier': tier,
        'acquisition_channel': channel,
        'signup_date': cohort_month + timedelta(days=random.randint(0, 28))
    })

df_customers = pd.DataFrame(customers)

# Generate subscription orders (monthly recurring)
orders = []
order_id = 1

for _, customer in df_customers.iterrows():
    signup = customer['signup_date']
    cohort = customer['cohort_month']
    tier = customer['tier']
    
    # Retention probability by tier
    if tier == 'Enterprise':
        retention_prob = 0.92
        base_price = 299
    elif tier == 'Pro':
        retention_prob = 0.85
        base_price = 99
    else:
        retention_prob = 0.75
        base_price = 29
    
    current_date = signup
    is_active = True
    month_num = 0
    
    while current_date <= end_date and is_active:
        orders.append({
            'order_id': order_id,
            'customer_id': customer['customer_id'],
            'order_date': current_date,
            'cohort_month': cohort,
            'tier': tier,
            'channel': customer['acquisition_channel'],
            'revenue': base_price + random.uniform(-5, 15),
            'month_number': month_num
        })
        
        order_id += 1
        month_num += 1
        current_date += timedelta(days=30)
        
        # Churn check (loyalty increases over time)
        retention_boost = min(month_num * 0.02, 0.15)
        if random.random() > (retention_prob + retention_boost):
            is_active = False

df_orders = pd.DataFrame(orders)

# Save files
df_customers.to_csv('cohort_customers.csv', index=False)
df_orders.to_csv('cohort_orders.csv', index=False)

print(f"✅ Generated {len(df_customers)} customers")
print(f"✅ Generated {len(df_orders)} orders")