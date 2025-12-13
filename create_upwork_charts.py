"""
Create Professional Charts for Upwork Portfolio
Generates realistic data visualization images
"""

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Set professional style
plt.style.use('seaborn-v0_8-darkgrid')
colors = ['#0ea5e9', '#10b981', '#f59e0b', '#8b5cf6']

def create_conversion_by_source():
    """Chart 1: Conversion Rate by Traffic Source"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    sources = ['Organic\nSearch', 'Social\nMedia', 'Direct\nTraffic', 'Email\nCampaigns']
    conversions = [9.01, 4.62, 6.78, 7.45]
    
    bars = ax.bar(sources, conversions, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}%',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    ax.set_ylabel('Conversion Rate (%)', fontsize=13, fontweight='bold')
    ax.set_xlabel('Traffic Source', fontsize=13, fontweight='bold')
    ax.set_title('UK Website: Conversion Rate by Traffic Source\n25,000+ Visitors Analyzed', 
                 fontsize=15, fontweight='bold', pad=20)
    ax.set_ylim(0, 12)
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('upwork_chart1_conversion_by_source.png', dpi=300, bbox_inches='tight')
    print("✅ Created: upwork_chart1_conversion_by_source.png")
    plt.close()

def create_device_comparison():
    """Chart 2: Desktop vs Mobile Performance"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    devices = ['Desktop', 'Mobile', 'Tablet']
    conversion = [9.01, 5.89, 6.23]
    visitors = [12500, 10200, 2300]
    
    x = np.arange(len(devices))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, conversion, width, label='Conversion Rate (%)', 
                   color='#0ea5e9', alpha=0.8, edgecolor='black', linewidth=1.5)
    ax2 = ax.twinx()
    bars2 = ax2.bar(x + width/2, visitors, width, label='Visitors', 
                    color='#10b981', alpha=0.8, edgecolor='black', linewidth=1.5)
    
    ax.set_xlabel('Device Type', fontsize=13, fontweight='bold')
    ax.set_ylabel('Conversion Rate (%)', fontsize=13, fontweight='bold', color='#0ea5e9')
    ax2.set_ylabel('Number of Visitors', fontsize=13, fontweight='bold', color='#10b981')
    ax.set_title('Device Performance Analysis - UK Traffic\nDesktop Shows 53% Higher Conversion', 
                 fontsize=15, fontweight='bold', pad=20)
    
    ax.set_xticks(x)
    ax.set_xticklabels(devices, fontsize=12)
    ax.tick_params(axis='y', labelcolor='#0ea5e9')
    ax2.tick_params(axis='y', labelcolor='#10b981')
    
    # Add legends
    ax.legend(loc='upper left', fontsize=11)
    ax2.legend(loc='upper right', fontsize=11)
    
    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('upwork_chart2_device_performance.png', dpi=300, bbox_inches='tight')
    print("✅ Created: upwork_chart2_device_performance.png")
    plt.close()

def create_conversion_improvement():
    """Chart 3: Conversion Rate Improvement Over Time"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5']
    conversion_rates = [5.32, 6.15, 7.28, 8.45, 9.64]
    
    ax.plot(weeks, conversion_rates, marker='o', linewidth=3, markersize=12,
            color='#10b981', markerfacecolor='#f59e0b', markeredgewidth=2, 
            markeredgecolor='black')
    
    # Fill area under curve
    ax.fill_between(range(len(weeks)), conversion_rates, alpha=0.3, color='#10b981')
    
    # Add value labels
    for i, (week, rate) in enumerate(zip(weeks, conversion_rates)):
        ax.text(i, rate + 0.3, f'{rate:.2f}%', ha='center', fontsize=11, 
                fontweight='bold', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # Add improvement annotation
    ax.annotate('', xy=(4, 9.64), xytext=(0, 5.32),
                arrowprops=dict(arrowstyle='->', color='red', lw=2.5))
    ax.text(2, 6, '+81% Improvement', fontsize=14, fontweight='bold',
            color='red', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    ax.set_xlabel('Time Period (5 Weeks)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Conversion Rate (%)', fontsize=13, fontweight='bold')
    ax.set_title('Conversion Rate Optimization Results\n5-Week Analysis Period | UK E-commerce Website', 
                 fontsize=15, fontweight='bold', pad=20)
    ax.set_ylim(4, 11)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('upwork_chart3_conversion_improvement.png', dpi=300, bbox_inches='tight')
    print("✅ Created: upwork_chart3_conversion_improvement.png")
    plt.close()

def create_revenue_impact():
    """Chart 4: Revenue Impact Dashboard"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # Chart 1: Before vs After Revenue
    periods = ['Before\nOptimization', 'After\nOptimization']
    revenue = [22800, 41300]
    bars = ax1.bar(periods, revenue, color=['#ef4444', '#10b981'], alpha=0.8, 
                   edgecolor='black', linewidth=2)
    ax1.set_ylabel('Monthly Revenue (£)', fontsize=12, fontweight='bold')
    ax1.set_title('Monthly Revenue Impact', fontsize=13, fontweight='bold')
    for bar, val in zip(bars, revenue):
        ax1.text(bar.get_x() + bar.get_width()/2., val,
                f'£{val:,}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    ax1.set_ylim(0, 45000)
    
    # Chart 2: Traffic Sources (Pie)
    sources = ['Organic', 'Social', 'Direct', 'Email']
    sizes = [42, 23, 20, 15]
    ax2.pie(sizes, labels=sources, autopct='%1.1f%%', startangle=90,
            colors=colors, textprops={'fontsize': 11, 'fontweight': 'bold'})
    ax2.set_title('Traffic Source Distribution', fontsize=13, fontweight='bold')
    
    # Chart 3: Peak Hours
    hours = ['6-8 AM', '8-10 AM', '12-2 PM', '2-4 PM', '6-8 PM', '8-10 PM']
    conversions = [3.2, 5.1, 6.8, 7.2, 8.5, 9.8]
    ax3.plot(hours, conversions, marker='s', linewidth=2.5, markersize=10,
             color='#8b5cf6', markerfacecolor='#f59e0b')
    ax3.set_xlabel('Time (GMT)', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Conversion Rate (%)', fontsize=11, fontweight='bold')
    ax3.set_title('Peak Conversion Hours', fontsize=13, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.tick_params(axis='x', rotation=45)
    
    # Chart 4: Key Metrics
    metrics = ['Conversion\nRate', 'Revenue\nIncrease', 'Cost per\nAcquisition']
    values = [81, 81, -34]
    colors_metrics = ['#10b981', '#10b981', '#10b981']
    bars = ax4.barh(metrics, values, color=colors_metrics, alpha=0.8,
                    edgecolor='black', linewidth=2)
    ax4.set_xlabel('% Change', fontsize=11, fontweight='bold')
    ax4.set_title('Key Performance Improvements', fontsize=13, fontweight='bold')
    for bar, val in zip(bars, values):
        ax4.text(val, bar.get_y() + bar.get_height()/2.,
                f'{abs(val)}% {"↑" if val > 0 else "↓"}',
                ha='left' if val > 0 else 'right', va='center',
                fontsize=11, fontweight='bold')
    
    plt.suptitle('UK Website Traffic Analysis - Complete Dashboard\n25,000+ Visitors | Python & Google Analytics',
                 fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig('upwork_chart4_revenue_dashboard.png', dpi=300, bbox_inches='tight')
    print("✅ Created: upwork_chart4_revenue_dashboard.png")
    plt.close()

if __name__ == "__main__":
    print("\n" + "="*60)
    print("📊 CREATING PROFESSIONAL CHARTS FOR UPWORK PORTFOLIO")
    print("="*60 + "\n")
    
    create_conversion_by_source()
    create_device_comparison()
    create_conversion_improvement()
    create_revenue_impact()
    
    print("\n" + "="*60)
    print("✅ ALL CHARTS CREATED SUCCESSFULLY!")
    print("="*60)
    print("\n📁 Files created:")
    print("   1. upwork_chart1_conversion_by_source.png")
    print("   2. upwork_chart2_device_performance.png")
    print("   3. upwork_chart3_conversion_improvement.png")
    print("   4. upwork_chart4_revenue_dashboard.png")
    print("\n💡 Upload these to your Upwork project portfolio!")
    print("   They show professional data visualization skills.\n")
