"""
UK E-Commerce Sales Data Generator
Creates realistic sales data for Excel dashboard project
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

print("\n" + "="*70)
print("UK E-COMMERCE SALES DATA GENERATOR")
print("Real Project - Serghei Covalciuc")
print("="*70 + "\n")

# Product categories with realistic UK pricing
categories = {
    'Electronics': {
        'products': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smart Watch'],
        'price_range': (50, 1200),
        'volume_weight': 3.0  # Higher sales volume
    },
    'Home & Garden': {
        'products': ['Coffee Maker', 'Vacuum Cleaner', 'Bedding Set', 'Garden Tools', 'Storage Box'],
        'price_range': (20, 300),
        'volume_weight': 2.5
    },
    'Fashion': {
        'products': ['Jacket', 'Trainers', 'Dress', 'Jeans', 'Handbag'],
        'price_range': (25, 250),
        'volume_weight': 2.0
    },
    'Sports': {
        'products': ['Yoga Mat', 'Dumbbells', 'Running Shoes', 'Gym Bag', 'Protein Powder'],
        'price_range': (15, 180),
        'volume_weight': 1.5
    }
}

# UK regions with different market sizes
regions = {
    'London': 0.30,      # 30% of sales
    'South East': 0.25,  # 25% of sales
    'North West': 0.20,  # 20% of sales
    'Scotland': 0.15,    # 15% of sales
    'Wales': 0.10        # 10% of sales
}

# Generate 6 months of data (Jan - June 2024)
start_date = datetime(2024, 1, 1)
sales_data = []
order_id = 1000

print("Generating sales records...")

for month in range(6):
    # Calculate days in month
    current_month = start_date + timedelta(days=30*month)
    days_in_month = 31 if month in [0, 2, 4] else 30
    
    # Base orders per day increases over time (growth trend)
    base_orders = 15 + (month * 3)  # Start at 15, increase by 3 per month
    
    for day in range(days_in_month):
        current_date = current_month + timedelta(days=day)
        
        # Weekends get more orders (realistic pattern)
        if current_date.weekday() >= 5:  # Saturday, Sunday
            daily_orders = int(base_orders * 1.3)
        else:
            daily_orders = base_orders
        
        for _ in range(daily_orders):
            # Select category based on weights
            category = random.choices(
                list(categories.keys()),
                weights=[cat['volume_weight'] for cat in categories.values()]
            )[0]
            
            # Select product and generate price
            product = random.choice(categories[category]['products'])
            price_min, price_max = categories[category]['price_range']
            unit_price = round(random.uniform(price_min, price_max), 2)
            
            # Quantity (most orders are 1-2 items)
            quantity = random.choices([1, 2, 3], weights=[0.7, 0.25, 0.05])[0]
            
            # Select region based on distribution
            region = random.choices(
                list(regions.keys()),
                weights=list(regions.values())
            )[0]
            
            # Calculate totals
            subtotal = round(unit_price * quantity, 2)
            
            sales_data.append({
                'Order_ID': f'ORD{order_id:05d}',
                'Date': current_date.strftime('%Y-%m-%d'),
                'Month': current_date.strftime('%B'),
                'Category': category,
                'Product': product,
                'Region': region,
                'Unit_Price': unit_price,
                'Quantity': quantity,
                'Total_Sales': subtotal
            })
            
            order_id += 1

# Create DataFrame
df = pd.DataFrame(sales_data)

print(f"✅ Generated {len(df)} sales records")
print(f"✅ Date range: {df['Date'].min()} to {df['Date'].max()}")
print(f"✅ Total revenue: £{df['Total_Sales'].sum():,.2f}\n")

# Save to CSV
df.to_csv('uk_ecommerce_sales_data.csv', index=False)
print("✅ Saved to: uk_ecommerce_sales_data.csv\n")

# Analysis
print("="*70)
print("QUICK ANALYSIS - UK E-COMMERCE SALES")
print("="*70 + "\n")

# Category breakdown
print("SALES BY CATEGORY:")
print("-" * 70)
category_sales = df.groupby('Category')['Total_Sales'].sum().sort_values(ascending=False)
for cat, sales in category_sales.items():
    percentage = (sales / category_sales.sum()) * 100
    print(f"{cat:20s} £{sales:>10,.2f}  ({percentage:5.1f}%)")

print("\n" + "-" * 70)
print("SALES BY REGION:")
print("-" * 70)
region_sales = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
for reg, sales in region_sales.items():
    percentage = (sales / region_sales.sum()) * 100
    print(f"{reg:20s} £{sales:>10,.2f}  ({percentage:5.1f}%)")

print("\n" + "-" * 70)
print("MONTHLY SALES TREND:")
print("-" * 70)
# Ensure months in correct order
month_order = ['January', 'February', 'March', 'April', 'May', 'June']
monthly_sales = df.groupby('Month')['Total_Sales'].sum()
monthly_sales = monthly_sales.reindex(month_order)

for month, sales in monthly_sales.items():
    print(f"{month:15s} £{sales:>10,.2f}")

# Calculate growth
jan_sales = monthly_sales.iloc[0]
jun_sales = monthly_sales.iloc[-1]
growth = ((jun_sales - jan_sales) / jan_sales) * 100

print(f"\n{'Growth (Jan-Jun)':15s} +{growth:.1f}%")

print("\n" + "="*70)
print("TOP SELLING PRODUCTS:")
print("="*70)
product_sales = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(5)
for i, (prod, sales) in enumerate(product_sales.items(), 1):
    print(f"{i}. {prod:20s} £{sales:>10,.2f}")

print("\n" + "="*70)
print("KEY METRICS:")
print("="*70)
print(f"Total Orders:        {len(df):,}")
print(f"Total Revenue:       £{df['Total_Sales'].sum():,.2f}")
print(f"Average Order Value: £{df['Total_Sales'].mean():.2f}")
print(f"Top Category:        {category_sales.index[0]} ({category_sales.iloc[0]/category_sales.sum()*100:.1f}%)")
print(f"Top Region:          {region_sales.index[0]} ({region_sales.iloc[0]/region_sales.sum()*100:.1f}%)")

print("\n" + "="*70)
print("✅ DATA GENERATION COMPLETE!")
print("="*70)
print("\nNext steps:")
print("1. Open uk_ecommerce_sales_data.csv in Excel")
print("2. Run python create_excel_dashboard.py to create dashboard")
print("3. Use PivotTables to analyze the data")
print("\n")
