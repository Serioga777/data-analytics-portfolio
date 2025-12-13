"""
Resize all charts for Upwork upload (max 4000x4000 pixels)
"""
from PIL import Image
import os

charts = [
    'upwork_chart1_conversion_by_source.png',
    'upwork_chart2_device_performance.png',
    'upwork_chart3_conversion_improvement.png',
    'upwork_chart4_revenue_dashboard.png'
]

max_width = 2400  # Safe size for Upwork

for chart in charts:
    if os.path.exists(chart):
        img = Image.open(chart)
        
        # Calculate new dimensions
        if img.width > max_width:
            new_width = max_width
            new_height = int(max_width * img.height / img.width)
            img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        else:
            img_resized = img
        
        # Save optimized version
        output_name = chart.replace('.png', '_upwork.png')
        img_resized.save(output_name, optimize=True, quality=95)
        print(f"✅ Created: {output_name} ({img_resized.width}x{img_resized.height})")

print("\n📤 Upload these files to Upwork:")
print("   - upwork_chart3_conversion_improvement_upwork.png (BEST - shows results)")
print("   - upwork_chart1_conversion_by_source_upwork.png (shows analysis)")
print("   - upwork_chart4_revenue_dashboard_upwork.png (comprehensive)")
