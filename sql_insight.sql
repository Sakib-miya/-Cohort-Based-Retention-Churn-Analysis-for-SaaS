create database cohort_retention_table;
use cohort_retention_table;
WITH first_purchase AS (
  SELECT 
    customer_id,
    DATE_FORMAT(MIN(order_date), '%Y-%m-01') as cohort_month
  FROM cohort_orders
  GROUP BY customer_id
),
monthly_activity AS (
  SELECT 
    f.cohort_month,
    DATE_FORMAT(o.order_date, '%Y-%m-01') as activity_month,
    COUNT(DISTINCT o.customer_id) as active_customers
  FROM first_purchase f
  JOIN cohort_orders o ON f.customer_id = o.customer_id
  GROUP BY f.cohort_month, DATE_FORMAT(o.order_date, '%Y-%m-01')
),
cohort_sizes AS (
  SELECT 
    cohort_month,
    COUNT(DISTINCT customer_id) as cohort_size
  FROM first_purchase
  GROUP BY cohort_month
)
SELECT 
  m.cohort_month,
  m.activity_month,
  TIMESTAMPDIFF(MONTH, m.cohort_month, m.activity_month) as months_since_signup,
  m.active_customers,
  c.cohort_size,
  ROUND(100.0 * m.active_customers / c.cohort_size, 2) as retention_rate
FROM monthly_activity m
JOIN cohort_sizes c ON m.cohort_month = c.cohort_month
ORDER BY m.cohort_month, m.activity_month;



SELECT 
  cohort_month,
  tier,
  COUNT(DISTINCT customer_id) as customers,
  ROUND(AVG(total_revenue), 2) as avg_ltv,
  ROUND(AVG(months_active), 2) as avg_lifetime_months,
  ROUND(AVG(total_revenue) / AVG(months_active), 2) as avg_revenue_per_month
FROM (
  SELECT 
    c.cohort_month,
    c.tier,
    o.customer_id,
    SUM(o.revenue) as total_revenue,
    COUNT(DISTINCT DATE_FORMAT(o.order_date, '%Y-%m-01')) as months_active
  FROM cohort_customers c
  JOIN cohort_orders o ON c.customer_id = o.customer_id
  GROUP BY c.cohort_month, c.tier, o.customer_id
) cohort_ltv
GROUP BY cohort_month, tier
ORDER BY cohort_month, tier;


WITH customer_last_activity AS (
  SELECT 
    customer_id,
    MAX(order_date) as last_order_date,
    COUNT(*) as total_orders
  FROM cohort_orders
  GROUP BY customer_id
)
SELECT 
  c.tier,
  COUNT(*) as total_customers,
  SUM(CASE WHEN l.last_order_date < CURDATE() - INTERVAL 60 DAY THEN 1 ELSE 0 END) as churned_customers,
  ROUND(100.0 * SUM(CASE WHEN l.last_order_date < CURDATE() - INTERVAL 60 DAY THEN 1 ELSE 0 END) / COUNT(*), 2) as churn_rate
FROM cohort_customers c
JOIN customer_last_activity l ON c.customer_id = l.customer_id
GROUP BY c.tier;




SELECT 
  acquisition_channel,
  COUNT(DISTINCT customer_id) as customers_acquired,
  ROUND(AVG(total_revenue), 2) as avg_ltv,
  ROUND(AVG(months_retained), 2) as avg_retention_months
FROM (
  SELECT 
    c.acquisition_channel,
    c.customer_id,
    SUM(o.revenue) as total_revenue,
    MAX(o.month_number) as months_retained
  FROM cohort_customers c
  JOIN cohort_orders o ON c.customer_id = o.customer_id
  GROUP BY c.acquisition_channel, c.customer_id
) channel_metrics
GROUP BY acquisition_channel
ORDER BY avg_ltv DESC;



