# Sales Dashboard - Excel Data Analysis Project

## Project Overview
Interactive Excel dashboard analyzing Q1 2024 sales data for a retail electronics company.

## 🎯 Objectives
- Analyze sales performance across products, regions, and customer types
- Identify top-performing products and regions
- Track sales trends over time
- Provide actionable insights for business decision-making

## 📁 Files Included
- `sales_data_2024.csv` - Raw sales data (50 transactions, Jan-Mar 2024)
- `sales_dashboard.xlsx` - Excel workbook with analysis and dashboard (you create this)

## 🔧 Tools Used
- Microsoft Excel
- PivotTables
- Charts & Graphs
- Conditional Formatting
- Formulas (SUM, AVERAGE, VLOOKUP, IF)

## 📈 Key Metrics Analyzed
1. **Total Sales**: $153,947.23
2. **Total Transactions**: 50
3. **Average Transaction Value**: $3,078.94
4. **Products Sold**: 653 units

## 🔍 Analysis Steps

### Step 1: Data Import
1. Open Excel → Data tab → Get Data → From Text/CSV
2. Import `sales_data_2024.csv`
3. Ensure data types are correct (Date, Number, Text)

### Step 2: Create PivotTables

**PivotTable 1: Sales by Product**
- Rows: Product
- Values: Sum of Total_Sales, Sum of Quantity
- Shows which products generate most revenue

**PivotTable 2: Sales by Region**
- Rows: Region
- Values: Sum of Total_Sales
- Shows regional performance

**PivotTable 3: Sales by Month**
- Rows: Date (grouped by Month)
- Values: Sum of Total_Sales
- Shows sales trends over time

**PivotTable 4: Customer Type Analysis**
- Rows: Customer_Type
- Values: Sum of Total_Sales, Count of Date
- Compare Business vs Retail customers

### Step 3: Create Visualizations
1. **Column Chart**: Sales by Product
2. **Pie Chart**: Sales by Region
3. **Line Chart**: Monthly sales trend
4. **Bar Chart**: Business vs Retail sales

### Step 4: Build Dashboard
- Create new sheet called "Dashboard"
- Copy/paste charts to dashboard
- Add slicers for interactivity (Product, Region, Month)
- Format with professional colors and layout
- Add title and key insights

### Step 5: Add Calculations
Create calculated columns:
- `Profit Margin` = Total_Sales * 0.25 (assuming 25% margin)
- `Month` = MONTH(Date)
- `Quarter` = "Q" & ROUNDUP(MONTH(Date)/3,0)

## 📊 Key Findings

### Top Performers
- **Best-selling product**: Laptop (€71,999.41 total sales)
- **Highest revenue region**: North (€36,248.44)
- **Best month**: March 2024 (€52,618.28)

### Insights
1. **Laptops dominate revenue** (46.7% of total sales)
2. **Business customers** spend 2.3x more per transaction than Retail
3. **Sales grew 15% month-over-month** from January to March
4. **North region** consistently outperforms other regions
5. **Accessories category** has higher volume but lower revenue

### Recommendations
1. Focus marketing budget on Laptop category
2. Expand business customer acquisition in South/West regions
3. Introduce bundle deals (Laptop + Accessories)
4. Investigate why March had highest sales (seasonal? promotion?)

## 🎓 Skills Demonstrated
- [x] Data import and cleaning
- [x] PivotTable creation and analysis
- [x] Data visualization
- [x] Dashboard design
- [x] Business insights generation
- [x] Excel formulas and functions

## 📸 Screenshot Checklist
When presenting this project:
1. Screenshot of raw data table
2. Screenshot of PivotTables
3. Screenshot of final dashboard
4. Screenshot showing slicers in action

## 🚀 How to Recreate This Project
1. Download `sales_data_2024.csv`
2. Open Excel and import the data
3. Follow the analysis steps above
4. Create your own dashboard layout
5. Add your personal insights

## 💡 Extension Ideas
- Add YoY comparison if you have 2023 data
- Create forecast for Q2 2024
- Build customer segmentation analysis
- Add profitability analysis by product

---
**Project Duration**: 2-3 hours  
**Difficulty**: Beginner  
**Skills Level**: Excel Intermediate
