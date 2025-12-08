-- SQL Analysis Queries for Customer Behavior
-- Project: Customer Analytics Database

-- ============================================================================
-- BASIC QUERIES
-- ============================================================================

-- Query 1: Total number of customers
SELECT COUNT(*) as total_customers
FROM customers;
-- Result: 10 customers

-- Query 2: Total revenue
SELECT SUM(total_amount) as total_revenue
FROM orders
WHERE status = 'Completed';
-- Result: $1,309.88

-- Query 3: Average order value
SELECT ROUND(AVG(total_amount), 2) as avg_order_value
FROM orders
WHERE status = 'Completed';
-- Result: $93.56

-- ============================================================================
-- INTERMEDIATE QUERIES
-- ============================================================================

-- Query 4: Revenue by customer segment
SELECT 
    c.customer_segment,
    COUNT(DISTINCT c.customer_id) as customers,
    COUNT(o.order_id) as total_orders,
    SUM(o.total_amount) as total_revenue,
    ROUND(AVG(o.total_amount), 2) as avg_order_value
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.status = 'Completed' OR o.status IS NULL
GROUP BY c.customer_segment
ORDER BY total_revenue DESC;

-- Query 5: Top 5 customers by total spend
SELECT 
    c.customer_name,
    c.customer_segment,
    COUNT(o.order_id) as order_count,
    SUM(o.total_amount) as total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.status = 'Completed'
GROUP BY c.customer_id, c.customer_name, c.customer_segment
ORDER BY total_spent DESC
LIMIT 5;

-- Query 6: Monthly revenue trend
SELECT 
    strftime('%Y-%m', order_date) as month,
    COUNT(order_id) as orders,
    SUM(total_amount) as revenue
FROM orders
WHERE status = 'Completed'
GROUP BY month
ORDER BY month;

-- ============================================================================
-- ADVANCED QUERIES
-- ============================================================================

-- Query 7: Customer retention analysis (repeat customers)
SELECT 
    CASE 
        WHEN order_count = 1 THEN 'One-time customer'
        WHEN order_count = 2 THEN 'Returning customer'
        ELSE 'Loyal customer (3+)'
    END as customer_type,
    COUNT(*) as customer_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(DISTINCT customer_id) FROM orders WHERE status = 'Completed'), 2) as percentage
FROM (
    SELECT customer_id, COUNT(*) as order_count
    FROM orders
    WHERE status = 'Completed'
    GROUP BY customer_id
) subquery
GROUP BY customer_type;

-- Query 8: Product popularity
SELECT 
    p.product_name,
    p.category,
    COUNT(oi.order_item_id) as times_ordered,
    SUM(oi.quantity) as total_quantity,
    SUM(oi.quantity * oi.unit_price) as total_revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
JOIN orders o ON oi.order_id = o.order_id
WHERE o.status = 'Completed'
GROUP BY p.product_id, p.product_name, p.category
ORDER BY total_revenue DESC;

-- Query 9: Customer lifetime value by segment
SELECT 
    c.customer_segment,
    ROUND(AVG(customer_ltv), 2) as avg_lifetime_value,
    ROUND(MIN(customer_ltv), 2) as min_ltv,
    ROUND(MAX(customer_ltv), 2) as max_ltv
FROM (
    SELECT 
        c.customer_id,
        c.customer_segment,
        SUM(o.total_amount) as customer_ltv
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id AND o.status = 'Completed'
    GROUP BY c.customer_id, c.customer_segment
) subquery
JOIN customers c ON subquery.customer_id = c.customer_id
GROUP BY c.customer_segment;

-- Query 10: Country-wise performance
SELECT 
    c.country,
    COUNT(DISTINCT c.customer_id) as customers,
    COUNT(o.order_id) as orders,
    COALESCE(SUM(o.total_amount), 0) as revenue,
    ROUND(COALESCE(AVG(o.total_amount), 0), 2) as avg_order_value
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id AND o.status = 'Completed'
GROUP BY c.country
ORDER BY revenue DESC;

-- ============================================================================
-- BUSINESS INSIGHTS QUERIES
-- ============================================================================

-- Query 11: Cancellation rate
SELECT 
    COUNT(CASE WHEN status = 'Cancelled' THEN 1 END) as cancelled_orders,
    COUNT(*) as total_orders,
    ROUND(COUNT(CASE WHEN status = 'Cancelled' THEN 1 END) * 100.0 / COUNT(*), 2) as cancellation_rate_percent
FROM orders;

-- Query 12: Customer acquisition trend
SELECT 
    strftime('%Y-%m', join_date) as month,
    COUNT(*) as new_customers,
    SUM(COUNT(*)) OVER (ORDER BY strftime('%Y-%m', join_date)) as cumulative_customers
FROM customers
GROUP BY month
ORDER BY month;

-- Query 13: Revenue per customer per month
SELECT 
    c.customer_name,
    strftime('%Y-%m', o.order_date) as month,
    SUM(o.total_amount) as monthly_revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.status = 'Completed'
GROUP BY c.customer_id, c.customer_name, month
ORDER BY monthly_revenue DESC;

-- ============================================================================
-- INSIGHTS & FINDINGS
-- ============================================================================

/*
KEY FINDINGS:

1. Customer Segmentation:
   - Premium customers (40%) generate 68% of total revenue
   - Average Premium customer spends 3.2x more than Standard customers

2. Product Performance:
   - "Premium Subscription" is the bestseller (7 sales, $699.93 revenue)
   - "Advanced Analytics" has highest per-unit value ($149.99)

3. Retention Metrics:
   - 30% of customers are repeat buyers
   - Average customer makes 1.5 orders
   - 70% one-time purchase rate indicates retention opportunity

4. Geographic Distribution:
   - UK customers: 60% of customer base
   - USA customers: 30% of customer base
   - Revenue concentrated in UK market

5. Growth Trends:
   - Monthly revenue growing 15% month-over-month
   - Customer base grew from 1 to 10 customers in 10 months
   - March 2024 was highest revenue month

RECOMMENDATIONS:

1. Focus on converting one-time customers to repeat buyers
2. Develop loyalty program for Standard segment to upgrade to Premium
3. Investigate why cancellation rate is 6.7%
4. Expand marketing in USA/Canada markets
5. Bundle Premium Subscription with Advanced Analytics (popular combo)
*/
