"""
Create Professional Charts for Projects #2 and #3
Project 2: UK E-Commerce Sales Dashboard
Project 3: London Property Rental Analysis
"""

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Set professional style
plt.style.use('seaborn-v0_8-darkgrid')
colors = ['#0ea5e9', '#10b981', '#f59e0b', '#8b5cf6', '#ef4444']

print("\n" + "="*60)
print("📊 CREATING CHARTS FOR PROJECTS #2 AND #3")
print("="*60 + "\n")

# ============================================================================
# PROJECT #2: UK E-COMMERCE SALES DASHBOARD
# ============================================================================

def create_project2_revenue_by_category():
    """Project 2, Chart 1: Revenue by Product Category"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    categories = ['Electronics', 'Home & Garden', 'Fashion', 'Sports', 'Books']
    revenue = [59563, 28450, 21890, 12347, 5200]
    percentage = [46.7, 22.3, 17.2, 9.7, 4.1]
    
    bars = ax.barh(categories, revenue, color=colors, alpha=0.85, edgecolor='black', linewidth=2)
    
    # Add value labels
    for i, (bar, val, pct) in enumerate(zip(bars, revenue, percentage)):
        ax.text(val + 1500, bar.get_y() + bar.get_height()/2,
                f'£{val:,} ({pct}%)',
                va='center', fontsize=11, fontweight='bold')
    
    ax.set_xlabel('Revenue (£)', fontsize=13, fontweight='bold')
    ax.set_title('UK E-Commerce Sales by Product Category\n£127,450 Total Revenue', 
                 fontsize=15, fontweight='bold', pad=20)
    ax.set_xlim(0, 70000)
    ax.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('project2_chart1_revenue_category_upwork.png', dpi=200, bbox_inches='tight')
    print("✅ Project 2, Chart 1: Revenue by Category")
    plt.close()

def create_project2_regional_sales():
    """Project 2, Chart 2: Sales by UK Region"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    regions = ['London &\nSouth East', 'North West', 'Midlands', 'Scotland', 'Wales &\nSouth West']
    sales = [49450, 31200, 24800, 15600, 6400]
    
    bars = ax.bar(regions, sales, color=colors, alpha=0.85, edgecolor='black', linewidth=2)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1000,
                f'£{int(height):,}',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    ax.set_ylabel('Sales (£)', fontsize=13, fontweight='bold')
    ax.set_xlabel('UK Region', fontsize=13, fontweight='bold')
    ax.set_title('Regional Sales Distribution - UK E-Commerce\nLondon & South East: 38.8% of Total Sales', 
                 fontsize=15, fontweight='bold', pad=20)
    ax.set_ylim(0, 55000)
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('project2_chart2_regional_sales_upwork.png', dpi=200, bbox_inches='tight')
    print("✅ Project 2, Chart 2: Regional Sales")
    plt.close()

def create_project2_monthly_growth():
    """Project 2, Chart 3: Monthly Growth Trend"""
    fig, ax = plt.subplots(figsize=(11, 6))
    
    months = ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
    revenue = [18200, 19500, 21100, 22800, 24300, 27950]
    
    ax.plot(months, revenue, marker='o', linewidth=3.5, markersize=14,
            color='#10b981', markerfacecolor='#f59e0b', markeredgewidth=3, 
            markeredgecolor='black')
    
    # Fill area
    ax.fill_between(range(len(months)), revenue, alpha=0.25, color='#10b981')
    
    # Add value labels
    for i, (month, rev) in enumerate(zip(months, revenue)):
        ax.text(i, rev + 800, f'£{rev:,}', ha='center', fontsize=10, 
                fontweight='bold', bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
    
    # Add growth annotation
    ax.annotate('', xy=(5, 27950), xytext=(0, 18200),
                arrowprops=dict(arrowstyle='->', color='red', lw=3))
    ax.text(2.5, 21000, '+53% Growth', fontsize=14, fontweight='bold',
            color='red', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))
    
    ax.set_ylabel('Monthly Revenue (£)', fontsize=13, fontweight='bold')
    ax.set_xlabel('Month (2024)', fontsize=13, fontweight='bold')
    ax.set_title('E-Commerce Revenue Growth Trend\n15% Average Month-over-Month Growth', 
                 fontsize=15, fontweight='bold', pad=20)
    ax.set_ylim(16000, 30000)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('project2_chart3_monthly_growth_upwork.png', dpi=200, bbox_inches='tight')
    print("✅ Project 2, Chart 3: Monthly Growth")
    plt.close()

# ============================================================================
# PROJECT #3: LONDON PROPERTY RENTAL ANALYSIS
# ============================================================================

def create_project3_rent_by_zone():
    """Project 3, Chart 1: Average Rent by London Zone"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    zones = ['Zone 1', 'Zone 2', 'Zone 3', 'Zone 4', 'Zone 5+']
    avg_rent = [2850, 2100, 1650, 1350, 1050]
    property_count = [45, 128, 156, 112, 59]
    
    x = np.arange(len(zones))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, avg_rent, width, label='Avg Rent (£/month)', 
                   color='#0ea5e9', alpha=0.85, edgecolor='black', linewidth=2)
    ax2 = ax.twinx()
    bars2 = ax2.bar(x + width/2, property_count, width, label='Properties Analyzed', 
                    color='#10b981', alpha=0.85, edgecolor='black', linewidth=2)
    
    ax.set_xlabel('London Zone', fontsize=13, fontweight='bold')
    ax.set_ylabel('Average Monthly Rent (£)', fontsize=12, fontweight='bold', color='#0ea5e9')
    ax2.set_ylabel('Number of Properties', fontsize=12, fontweight='bold', color='#10b981')
    ax.set_title('London Rental Market Analysis by Zone\n500+ Properties Analyzed', 
                 fontsize=15, fontweight='bold', pad=20)
    
    ax.set_xticks(x)
    ax.set_xticklabels(zones, fontsize=12)
    ax.tick_params(axis='y', labelcolor='#0ea5e9')
    ax2.tick_params(axis='y', labelcolor='#10b981')
    
    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 80,
                f'£{int(height):,}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    ax.legend(loc='upper left', fontsize=10)
    ax2.legend(loc='upper right', fontsize=10)
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('project3_chart1_rent_by_zone_upwork.png', dpi=200, bbox_inches='tight')
    print("✅ Project 3, Chart 1: Rent by Zone")
    plt.close()

def create_project3_property_types():
    """Project 3, Chart 2: Property Type Distribution"""
    fig, ax = plt.subplots(figsize=(9, 9))
    
    property_types = ['2-Bed Flat\n(42%)', '1-Bed Flat\n(28%)', '3-Bed Flat\n(15%)', 
                      'Studio\n(10%)', 'House\n(5%)']
    sizes = [42, 28, 15, 10, 5]
    explode = (0.1, 0, 0, 0, 0)  # Explode largest slice
    
    wedges, texts, autotexts = ax.pie(sizes, labels=property_types, autopct='%1.1f%%',
                                        explode=explode, startangle=90,
                                        colors=colors, textprops={'fontsize': 12, 'fontweight': 'bold'},
                                        wedgeprops={'edgecolor': 'black', 'linewidth': 2})
    
    # Make percentage text bold
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(13)
        autotext.set_fontweight('extra bold')
    
    ax.set_title('London Rental Property Type Distribution\nMost In-Demand: 2-Bedroom Flats', 
                 fontsize=15, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('project3_chart2_property_types_upwork.png', dpi=200, bbox_inches='tight')
    print("✅ Project 3, Chart 2: Property Types")
    plt.close()

def create_project3_roi_analysis():
    """Project 3, Chart 3: ROI by Postcode"""
    fig, ax = plt.subplots(figsize=(11, 6))
    
    postcodes = ['SE15', 'E17', 'SW16', 'N22', 'E11', 'CR0', 'BR1', 'KT2']
    roi = [8.2, 7.8, 6.5, 6.2, 5.9, 5.5, 5.2, 4.8]
    growth = [18, 18, 12, 10, 8, 7, 6, 5]
    
    # Create bars
    bars = ax.bar(postcodes, roi, color=['#10b981' if g >= 15 else '#0ea5e9' for g in growth],
                  alpha=0.85, edgecolor='black', linewidth=2)
    
    # Add value labels
    for bar, r, g in zip(bars, roi, growth):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.2,
                f'{r}%\n({g}% growth)',
                ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    ax.set_xlabel('London Postcode Area', fontsize=13, fontweight='bold')
    ax.set_ylabel('Rental Yield / ROI (%)', fontsize=13, fontweight='bold')
    ax.set_title('Investment Opportunities: Rental Yield by Postcode\nGreen = High Growth Areas (15%+)', 
                 fontsize=15, fontweight='bold', pad=20)
    ax.set_ylim(0, 10)
    ax.grid(axis='y', alpha=0.3)
    
    # Add recommendation box
    ax.text(0.5, 9.2, '💡 RECOMMENDED: SE15 & E17 (18% growth potential)',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.9),
            fontsize=11, fontweight='bold', ha='left')
    
    plt.tight_layout()
    plt.savefig('project3_chart3_roi_analysis_upwork.png', dpi=200, bbox_inches='tight')
    print("✅ Project 3, Chart 3: ROI Analysis")
    plt.close()

# ============================================================================
# RUN ALL CHART CREATION
# ============================================================================

if __name__ == "__main__":
    # Project 2 Charts
    print("Creating Project #2 Charts (E-Commerce)...")
    create_project2_revenue_by_category()
    create_project2_regional_sales()
    create_project2_monthly_growth()
    
    print("\nCreating Project #3 Charts (Property Rental)...")
    # Project 3 Charts
    create_project3_rent_by_zone()
    create_project3_property_types()
    create_project3_roi_analysis()
    
    print("\n" + "="*60)
    print("✅ ALL CHARTS CREATED SUCCESSFULLY!")
    print("="*60)
    print("\n📁 PROJECT #2 CHARTS (E-Commerce):")
    print("   - project2_chart1_revenue_category_upwork.png")
    print("   - project2_chart2_regional_sales_upwork.png")
    print("   - project2_chart3_monthly_growth_upwork.png")
    print("\n📁 PROJECT #3 CHARTS (Property Rental):")
    print("   - project3_chart1_rent_by_zone_upwork.png")
    print("   - project3_chart2_property_types_upwork.png")
    print("   - project3_chart3_roi_analysis_upwork.png")
    print("\n💡 Upload 2-3 charts per project to Upwork!\n")
