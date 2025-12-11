"""
London Property Rental Analysis - Data Generator
Creates realistic property rental data for SQL analysis
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

print("\n" + "="*70)
print("LONDON PROPERTY RENTAL ANALYSIS - DATA GENERATOR")
print("Real Project - Serghei Covalciuc")
print("="*70 + "\n")

# London postcodes with average rent characteristics
postcodes = {
    # Central London (expensive)
    'SW1': {'zone': 1, 'avg_rent': 2800, 'variance': 500},
    'WC1': {'zone': 1, 'avg_rent': 2650, 'variance': 450},
    'EC1': {'zone': 1, 'avg_rent': 2900, 'variance': 550},
    
    # Inner London (moderate-high)
    'N1': {'zone': 2, 'avg_rent': 2100, 'variance': 400},
    'E1': {'zone': 2, 'avg_rent': 1950, 'variance': 350},
    'SW9': {'zone': 2, 'avg_rent': 1850, 'variance': 300},
    'SE1': {'zone': 2, 'avg_rent': 2000, 'variance': 380},
    
    # Outer London (affordable)
    'SE15': {'zone': 3, 'avg_rent': 1450, 'variance': 250},  # UNDERVALUED
    'E17': {'zone': 3, 'avg_rent': 1380, 'variance': 220},   # UNDERVALUED
    'N22': {'zone': 3, 'avg_rent': 1500, 'variance': 240},
    'SW16': {'zone': 3, 'avg_rent': 1520, 'variance': 260},
    'SE23': {'zone': 3, 'avg_rent': 1480, 'variance': 230},
}

# Property types
property_types = {
    'Studio': {'beds': 0, 'rent_multiplier': 0.65, 'weight': 2},
    '1-Bed Flat': {'beds': 1, 'rent_multiplier': 1.0, 'weight': 4},
    '2-Bed Flat': {'beds': 2, 'rent_multiplier': 1.4, 'weight': 3},
    '3-Bed House': {'beds': 3, 'rent_multiplier': 1.8, 'weight': 1},
}

# Amenities affecting price
amenities = ['Furnished', 'Parking', 'Garden', 'Balcony', 'Recently Renovated']

print("Generating property rental data...")

properties = []
property_id = 1

# Generate 500+ properties
for postcode, details in postcodes.items():
    # Number of properties per postcode
    num_properties = random.randint(35, 55)
    
    for _ in range(num_properties):
        # Select property type
        prop_type = random.choices(
            list(property_types.keys()),
            weights=[pt['weight'] for pt in property_types.values()]
        )[0]
        
        # Calculate base rent
        base_rent = details['avg_rent'] * property_types[prop_type]['rent_multiplier']
        
        # Add variance
        rent = base_rent + random.gauss(0, details['variance'])
        
        # Add amenity bonuses
        property_amenities = random.sample(amenities, k=random.randint(1, 3))
        amenity_bonus = len(property_amenities) * 50
        rent += amenity_bonus
        
        # Add listing date (properties listed over past 6 months)
        days_ago = random.randint(0, 180)
        listed_date = datetime.now() - timedelta(days=days_ago)
        
        # Occupancy status (90% occupied)
        is_occupied = random.random() < 0.90
        
        # Calculate potential ROI based on zone
        if details['zone'] == 1:
            roi_potential = random.uniform(3.5, 5.0)  # Central London
        elif details['zone'] == 2:
            roi_potential = random.uniform(5.5, 7.5)  # Inner London
        else:
            roi_potential = random.uniform(8.0, 12.0)  # Outer London (BEST ROI)
        
        properties.append({
            'Property_ID': f'PROP{property_id:04d}',
            'Postcode': postcode,
            'Zone': details['zone'],
            'Property_Type': prop_type,
            'Bedrooms': property_types[prop_type]['beds'],
            'Monthly_Rent': round(rent, 2),
            'Amenities': ', '.join(property_amenities),
            'Listed_Date': listed_date.strftime('%Y-%m-%d'),
            'Is_Occupied': 'Yes' if is_occupied else 'No',
            'ROI_Potential': round(roi_potential, 2)
        })
        
        property_id += 1

# Create DataFrame
df = pd.DataFrame(properties)

print(f"✅ Generated {len(df)} property records")
print(f"✅ Date range: {df['Listed_Date'].min()} to {df['Listed_Date'].max()}")
print(f"✅ Average rent: £{df['Monthly_Rent'].mean():,.2f}/month\n")

# Save to CSV
df.to_csv('london_property_rentals.csv', index=False)
print("✅ Saved to: london_property_rentals.csv\n")

# Analysis
print("="*70)
print("SQL-STYLE ANALYSIS - LONDON PROPERTY RENTALS")
print("="*70 + "\n")

# Analysis 1: Average rent by zone
print("QUERY 1: Average Monthly Rent by Zone")
print("-" * 70)
zone_analysis = df.groupby('Zone').agg({
    'Monthly_Rent': ['mean', 'count']
}).round(2)
zone_analysis.columns = ['Avg_Rent', 'Property_Count']
print(zone_analysis.to_string())

# Analysis 2: Best postcodes by ROI
print("\n" + "-" * 70)
print("QUERY 2: Top 5 Postcodes by ROI Potential (Investment Opportunity)")
print("-" * 70)
postcode_roi = df.groupby('Postcode').agg({
    'ROI_Potential': 'mean',
    'Monthly_Rent': 'mean',
    'Property_ID': 'count'
}).round(2)
postcode_roi.columns = ['Avg_ROI', 'Avg_Rent', 'Properties']
postcode_roi = postcode_roi.sort_values('Avg_ROI', ascending=False).head(5)
print(postcode_roi.to_string())

# Analysis 3: Property type distribution
print("\n" + "-" * 70)
print("QUERY 3: Property Type Distribution and Average Rent")
print("-" * 70)
type_analysis = df.groupby('Property_Type').agg({
    'Monthly_Rent': 'mean',
    'Property_ID': 'count',
    'ROI_Potential': 'mean'
}).round(2)
type_analysis.columns = ['Avg_Rent', 'Count', 'Avg_ROI']
type_analysis = type_analysis.sort_values('Count', ascending=False)
print(type_analysis.to_string())

# Analysis 4: Undervalued areas (Zone 3 with high ROI)
print("\n" + "-" * 70)
print("QUERY 4: Undervalued Postcodes (Zone 3 with ROI > 10%)")
print("-" * 70)
undervalued = df[df['Zone'] == 3].groupby('Postcode').agg({
    'ROI_Potential': 'mean',
    'Monthly_Rent': 'mean',
    'Property_ID': 'count'
}).round(2)
undervalued.columns = ['Avg_ROI', 'Avg_Rent', 'Properties']
undervalued = undervalued[undervalued['Avg_ROI'] > 10.0].sort_values('Avg_ROI', ascending=False)
print(undervalued.to_string())

print("\n" + "="*70)
print("KEY FINDINGS:")
print("="*70)
print(f"📊 Total Properties Analyzed: {len(df)}")
print(f"📊 Average Monthly Rent: £{df['Monthly_Rent'].mean():.2f}")
print(f"📊 Occupancy Rate: {(df['Is_Occupied'] == 'Yes').sum() / len(df) * 100:.1f}%")

# Best investment areas
best_roi_postcode = postcode_roi.index[0]
best_roi_value = postcode_roi.iloc[0]['Avg_ROI']
print(f"\n⭐ Best Investment Area: {best_roi_postcode} (ROI: {best_roi_value}%)")

# Undervalued areas
undervalued_areas = undervalued.head(2).index.tolist()
print(f"⭐ Undervalued Areas: {', '.join(undervalued_areas)}")

# Zone comparison
zone1_avg = df[df['Zone'] == 1]['Monthly_Rent'].mean()
zone3_avg = df[df['Zone'] == 3]['Monthly_Rent'].mean()
savings = ((zone1_avg - zone3_avg) / zone1_avg) * 100
print(f"\n💷 RENT COMPARISON:")
print(f"   Zone 1 (Central): £{zone1_avg:.2f}/month")
print(f"   Zone 3 (Outer): £{zone3_avg:.2f}/month")
print(f"   Savings: {savings:.1f}% cheaper in Zone 3")

# ROI comparison
zone1_roi = df[df['Zone'] == 1]['ROI_Potential'].mean()
zone3_roi = df[df['Zone'] == 3]['ROI_Potential'].mean()
roi_boost = ((zone3_roi - zone1_roi) / zone1_roi) * 100
print(f"\n📈 ROI COMPARISON:")
print(f"   Zone 1 ROI: {zone1_roi:.1f}%")
print(f"   Zone 3 ROI: {zone3_roi:.1f}%")
print(f"   Zone 3 ROI is {roi_boost:.0f}% better!")

print("\n" + "="*70)
print("✅ DATA GENERATION COMPLETE!")
print("="*70)
print("\nNext steps:")
print("1. Import CSV to SQLite database")
print("2. Run python create_sql_analysis.py for advanced queries")
print("3. Use SQL to find investment opportunities")
print("\n")
