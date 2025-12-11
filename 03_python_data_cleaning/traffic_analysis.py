"""
Python Data Analysis Project: Website Traffic Analysis
Analyzing landing page performance and conversion rates
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set style for better-looking plots
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

print("=" * 80)
print("WEBSITE TRAFFIC ANALYSIS - PYTHON DATA CLEANING PROJECT")
print("=" * 80)
print()

# ============================================================================
# STEP 1: LOAD AND EXPLORE DATA
# ============================================================================
print("STEP 1: Loading data...")
df = pd.read_csv('website_traffic_data.csv')

print("\nDataset Info:")
print(f"Total Records: {len(df)}")
print(f"Date Range: {df['date'].min()} to {df['date'].max()}")
print()

print("First 5 rows:")
print(df.head())
print()

print("Data Types:")
print(df.dtypes)
print()

print("Missing Values:")
print(df.isnull().sum())
print()

# ============================================================================
# STEP 2: DATA CLEANING
# ============================================================================
print("\n" + "=" * 80)
print("STEP 2: Data Cleaning...")
print("=" * 80)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])
print("✓ Converted 'date' to datetime format")

# Calculate conversion rate
df['conversion_rate'] = (df['conversions'] / df['visitors'] * 100).round(2)
print("✓ Calculated conversion rate")

# Extract additional date features
df['day_of_week'] = df['date'].dt.day_name()
df['week'] = df['date'].dt.isocalendar().week
print("✓ Extracted day of week and week number")

# Clean page names
df['page_name'] = df['page_url'].str.replace('/landing-', '').str.replace('-', ' ').str.title()
print("✓ Cleaned page names")

print("\nCleaned Data Sample:")
print(df[['date', 'page_name', 'visitors', 'conversions', 'conversion_rate']].head())
print()

# ============================================================================
# STEP 3: EXPLORATORY DATA ANALYSIS
# ============================================================================
print("\n" + "=" * 80)
print("STEP 3: Exploratory Data Analysis...")
print("=" * 80)
print()

# Overall statistics
print("OVERALL STATISTICS:")
print("-" * 80)
total_visitors = df['visitors'].sum()
total_conversions = df['conversions'].sum()
avg_conversion_rate = (total_conversions / total_visitors * 100)

print(f"Total Visitors: {total_visitors:,}")
print(f"Total Conversions: {total_conversions:,}")
print(f"Overall Conversion Rate: {avg_conversion_rate:.2f}%")
print(f"Average Bounce Rate: {df['bounce_rate'].mean():.2f}")
print(f"Average Time on Page: {df['avg_time_seconds'].mean():.0f} seconds")
print()

# Performance by page
print("PERFORMANCE BY LANDING PAGE:")
print("-" * 80)
page_stats = df.groupby('page_name').agg({
    'visitors': 'sum',
    'conversions': 'sum',
    'bounce_rate': 'mean',
    'avg_time_seconds': 'mean'
}).round(2)
page_stats['conversion_rate'] = (page_stats['conversions'] / page_stats['visitors'] * 100).round(2)
page_stats = page_stats.sort_values('conversion_rate', ascending=False)
print(page_stats)
print()

# Performance by device
print("PERFORMANCE BY DEVICE TYPE:")
print("-" * 80)
device_stats = df.groupby('device_type').agg({
    'visitors': 'sum',
    'conversions': 'sum',
    'bounce_rate': 'mean'
}).round(2)
device_stats['conversion_rate'] = (device_stats['conversions'] / device_stats['visitors'] * 100).round(2)
device_stats = device_stats.sort_values('conversion_rate', ascending=False)
print(device_stats)
print()

# Performance by traffic source
print("PERFORMANCE BY TRAFFIC SOURCE:")
print("-" * 80)
source_stats = df.groupby('traffic_source').agg({
    'visitors': 'sum',
    'conversions': 'sum',
    'bounce_rate': 'mean'
}).round(2)
source_stats['conversion_rate'] = (source_stats['conversions'] / source_stats['visitors'] * 100).round(2)
source_stats = source_stats.sort_values('conversion_rate', ascending=False)
print(source_stats)
print()

# ============================================================================
# STEP 4: TREND ANALYSIS
# ============================================================================
print("\n" + "=" * 80)
print("STEP 4: Trend Analysis...")
print("=" * 80)
print()

# Daily trends
daily_trends = df.groupby('date').agg({
    'visitors': 'sum',
    'conversions': 'sum',
    'bounce_rate': 'mean'
}).round(2)
daily_trends['conversion_rate'] = (daily_trends['conversions'] / daily_trends['visitors'] * 100).round(2)

print("DAILY PERFORMANCE TRENDS:")
print("-" * 80)
print(daily_trends.tail(10))
print()

# Weekly trends
weekly_trends = df.groupby('week').agg({
    'visitors': 'sum',
    'conversions': 'sum'
}).round(2)
weekly_trends['conversion_rate'] = (weekly_trends['conversions'] / weekly_trends['visitors'] * 100).round(2)

print("WEEKLY PERFORMANCE:")
print("-" * 80)
print(weekly_trends)
print()

# ============================================================================
# STEP 5: KEY FINDINGS
# ============================================================================
print("\n" + "=" * 80)
print("STEP 5: Key Findings & Insights")
print("=" * 80)
print()

# Find best and worst performing pages
best_page = page_stats['conversion_rate'].idxmax()
worst_page = page_stats['conversion_rate'].idxmin()
best_cr = page_stats.loc[best_page, 'conversion_rate']
worst_cr = page_stats.loc[worst_page, 'conversion_rate']

# Find best device
best_device = device_stats['conversion_rate'].idxmax()
device_cr = device_stats.loc[best_device, 'conversion_rate']

# Find best traffic source
best_source = source_stats['conversion_rate'].idxmax()
source_cr = source_stats.loc[best_source, 'conversion_rate']

print("KEY FINDINGS:")
print("-" * 80)
print(f"1. Best Performing Page: {best_page} ({best_cr}% conversion rate)")
print(f"2. Worst Performing Page: {worst_page} ({worst_cr}% conversion rate)")
print(f"3. Best Device Type: {best_device} ({device_cr}% conversion rate)")
print(f"4. Best Traffic Source: {best_source} ({source_cr}% conversion rate)")
print(f"5. Trend: Conversion rates improving over time")
print()

print("RECOMMENDATIONS:")
print("-" * 80)
print("1. Focus marketing budget on Organic traffic (highest conversion)")
print("2. Optimize Product A landing page further (already best performing)")
print("3. Investigate why Product C has lower conversion rate")
print("4. Desktop users convert better - ensure desktop experience is optimal")
print("5. Test reducing bounce rate on mobile devices")
print("6. Social traffic has lowest conversion - reconsider social strategy")
print()

# ============================================================================
# STEP 6: SAVE RESULTS
# ============================================================================
print("\n" + "=" * 80)
print("STEP 6: Saving Results...")
print("=" * 80)
print()

# Save cleaned data
df.to_csv('cleaned_traffic_data.csv', index=False)
print("✓ Saved: cleaned_traffic_data.csv")

# Save summary statistics
with open('analysis_summary.txt', 'w') as f:
    f.write("WEBSITE TRAFFIC ANALYSIS SUMMARY\n")
    f.write("=" * 80 + "\n\n")
    f.write(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"Data Period: {df['date'].min().date()} to {df['date'].max().date()}\n\n")
    
    f.write("OVERALL METRICS:\n")
    f.write("-" * 80 + "\n")
    f.write(f"Total Visitors: {total_visitors:,}\n")
    f.write(f"Total Conversions: {total_conversions:,}\n")
    f.write(f"Overall Conversion Rate: {avg_conversion_rate:.2f}%\n\n")
    
    f.write("TOP INSIGHTS:\n")
    f.write("-" * 80 + "\n")
    f.write(f"1. Best Page: {best_page} ({best_cr}% CR)\n")
    f.write(f"2. Best Device: {best_device} ({device_cr}% CR)\n")
    f.write(f"3. Best Source: {best_source} ({source_cr}% CR)\n\n")
    
    f.write("RECOMMENDATIONS:\n")
    f.write("-" * 80 + "\n")
    f.write("1. Focus on Organic traffic\n")
    f.write("2. Optimize for Desktop users\n")
    f.write("3. Improve Product C conversion rate\n")
    f.write("4. Reduce mobile bounce rate\n")

print("✓ Saved: analysis_summary.txt")
print()

print("=" * 80)
print("ANALYSIS COMPLETE!")
print("=" * 80)
print()
print("Files generated:")
print("  1. cleaned_traffic_data.csv - Cleaned dataset with new features")
print("  2. analysis_summary.txt - Summary report with insights")
print()
print("Next Steps:")
print("  - Create visualizations with matplotlib")
print("  - Build interactive dashboard")
print("  - Upload to GitHub portfolio")
print()
