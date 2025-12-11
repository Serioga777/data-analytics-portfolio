# SQL Customer Behavior Analysis Project

## Project Overview
Comprehensive SQL analysis of customer behavior, purchase patterns, and business metrics for a SaaS company.

## 🎯 Objectives
- Analyze customer segmentation and lifetime value
- Identify purchasing patterns and trends
- Calculate key business metrics (retention, churn, revenue)
- Provide data-driven recommendations

## 🗄️ Database Structure

### Tables:
1. **customers** - Customer information and segmentation
2. **orders** - Order transactions and status
3. **products** - Product catalog
4. **order_items** - Detailed order line items

### Entity Relationship:
- One customer can have many orders
- One order can have many order items
- One product can appear in many order items

## 📁 Files Included
- `database_setup.sql` - Database schema and sample data
- `analysis_queries.sql` - 13 analytical queries with results
- `README.md` - This file

## 🔧 Tools Used
- SQLite / MySQL / PostgreSQL
- SQL (SELECT, JOIN, GROUP BY, Window Functions)
- Aggregate functions (COUNT, SUM, AVG)
- Subqueries and CTEs

## 📈 Key Metrics Analyzed

1. **Revenue Metrics**
   - Total Revenue: $1,309.88
   - Average Order Value: $93.56
   - Revenue by Segment, Country, Month

2. **Customer Metrics**
   - Total Customers: 10
   - Customer Lifetime Value by Segment
   - Repeat Customer Rate: 30%
   - One-time Purchase Rate: 70%

3. **Product Metrics**
   - Top-selling products
   - Revenue by category
   - Product performance analysis

## 🔍 SQL Queries Categories

### Basic Queries (1-3)
- Total customers count
- Total revenue calculation
- Average order value

### Intermediate Queries (4-6)
- Revenue by customer segment
- Top 5 customers by spend
- Monthly revenue trends

### Advanced Queries (7-10)
- Customer retention analysis
- Product popularity ranking
- Customer lifetime value calculation
- Geographic performance analysis

### Business Insights (11-13)
- Cancellation rate analysis
- Customer acquisition trends
- Revenue per customer tracking

## 📊 Key Findings

### Customer Segmentation
- **Premium Segment**: 40% of customers, 68% of revenue
- **Standard Segment**: 40% of customers, 25% of revenue
- **Basic Segment**: 20% of customers, 7% of revenue

### Product Insights
- Premium Subscription: Best-seller (7 orders, $699.93)
- Advanced Analytics: Highest value per sale ($149.99)
- Services category: 76% of total revenue

### Geographic Distribution
- UK: 60% of customers, 52% of revenue
- USA: 30% of customers, 35% of revenue
- Canada: 10% of customers, 13% of revenue

### Growth Trends
- 15% month-over-month revenue growth
- March 2024: Highest revenue month ($549.93)
- Consistent customer acquisition (1 customer/month avg)

## 🎓 SQL Skills Demonstrated
- [x] Database design and normalization
- [x] Complex JOINs (INNER, LEFT)
- [x] Aggregate functions (SUM, AVG, COUNT)
- [x] GROUP BY with multiple columns
- [x] Subqueries and derived tables
- [x] Window functions (OVER, SUM)
- [x] CASE statements for conditional logic
- [x] Date functions (strftime)
- [x] CTEs (Common Table Expressions)

## 🚀 How to Run This Project

### Option 1: SQLite (Easiest)
```bash
# Install SQLite (usually pre-installed on Mac/Linux)
# Windows: Download from sqlite.org

# Create database
sqlite3 customer_analytics.db

# Run setup script
.read database_setup.sql

# Run queries
.read analysis_queries.sql

# Or run individual queries
SELECT * FROM customers;
```

### Option 2: MySQL
```bash
# Create database
mysql -u root -p
CREATE DATABASE customer_analytics;
USE customer_analytics;

# Run setup
source database_setup.sql;

# Run queries
source analysis_queries.sql;
```

### Option 3: Online SQL Editor
- db-fiddle.com
- sqliteonline.com
- Copy-paste database_setup.sql, then run queries

## 💡 Recommendations Based on Analysis

1. **Improve Retention**
   - Create loyalty program for repeat purchases
   - Target one-time buyers with re-engagement campaigns
   - Offer discounts for second purchase

2. **Upsell Opportunities**
   - 60% of Standard customers could be upgraded to Premium
   - Bundle Premium Subscription + Advanced Analytics (popular combo)
   - Offer free trial of premium features to Standard users

3. **Geographic Expansion**
   - USA market shows high avg order value - invest more in marketing
   - Canada has small customer base but high engagement - opportunity to grow
   - Consider localized pricing for different regions

4. **Product Strategy**
   - Focus inventory on Premium Subscription and Advanced Analytics
   - Phase out or improve underperforming products
   - Create product bundles to increase average order value

5. **Reduce Cancellations**
   - Current cancellation rate: 6.7%
   - Investigate reasons (survey cancelled orders)
   - Implement better onboarding process

## 📸 Deliverables
- Database schema diagram
- Screenshots of query results
- Excel/Google Sheets with exported data
- Summary presentation with insights

## 🔗 Extensions
- Add customer churn prediction model
- Build cohort retention analysis
- Create RFM (Recency, Frequency, Monetary) segmentation
- Analyze seasonal trends with more data
- Build automated reporting dashboard

---
**Project Duration**: 3-4 hours  
**Difficulty**: Intermediate  
**Skills Level**: SQL Intermediate-Advanced
