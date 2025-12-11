# Python Data Cleaning & Analysis Project

## Project Overview
This project demonstrates Python skills for data cleaning, analysis, and deriving business insights from website traffic data. I analyzed landing page performance data from 50+ pages to identify factors that influence conversion rates.

## Business Question
**"What factors influence landing page conversion rates, and how can we optimize our digital marketing strategy?"**

## Dataset
- **File**: `website_traffic_data.csv`
- **Records**: 50 landing page sessions
- **Time Period**: January 1, 2024 - January 31, 2024
- **Metrics**: Visitors, Page Views, Bounce Rate, Time on Page, Conversions, Device Type, Traffic Source

### Data Dictionary
| Column | Description |
|--------|-------------|
| date | Date of the session |
| page_url | Landing page URL |
| visitors | Number of unique visitors |
| page_views | Total page views |
| bounce_rate | Percentage of single-page sessions |
| avg_time_seconds | Average time spent on page (seconds) |
| conversions | Number of conversions (sign-ups, purchases, etc.) |
| device_type | Device used (Desktop, Mobile, Tablet) |
| traffic_source | Where visitors came from (Organic, Paid Ads, Social, Email) |

## Tools & Libraries Used
- **Python 3.x**
- **pandas**: Data manipulation and cleaning
- **matplotlib** (optional): Data visualization
- **seaborn** (optional): Statistical visualizations

## How to Run This Project

### Option 1: Basic Analysis (No Additional Libraries Required)
```bash
python traffic_analysis.py
```

This will:
1. Load and explore the raw data
2. Clean and transform the data
3. Calculate key metrics and statistics
4. Generate insights and recommendations
5. Save cleaned data and summary report

### Option 2: Full Analysis with Visualizations
If you have matplotlib and seaborn installed:
```bash
pip install pandas matplotlib seaborn
python traffic_analysis.py
```

## Key Findings

### 1. Overall Performance
- **Total Visitors**: 1,268
- **Total Conversions**: 1,238
- **Overall Conversion Rate**: 97.63%
- **Average Bounce Rate**: 49.70%
- **Average Time on Page**: 109 seconds

### 2. Performance by Landing Page
| Page | Conversion Rate | Bounce Rate |
|------|----------------|-------------|
| **Product A** | ~98%+ | Improving (68% → 39%) |
| Product B | ~97% | Moderate |
| Product C | ~97% | Higher |

**Insight**: Product A shows the best performance and continuous improvement over time. Conversions grew from 12 to 61 throughout January.

### 3. Performance by Device Type
| Device | Conversion Rate | Traffic Share |
|--------|----------------|---------------|
| **Desktop** | Highest | ~35% |
| Mobile | Good | ~45% |
| Tablet | Good | ~20% |

**Insight**: Desktop users have the highest conversion rate. Mobile traffic is the largest segment but has slightly lower conversion rates.

### 4. Performance by Traffic Source
| Source | Conversion Rate | Quality |
|--------|----------------|---------|
| **Organic** | Highest | Best ROI |
| Email | High | Engaged audience |
| Paid Ads | Moderate | Review targeting |
| Social | Lower | Needs optimization |

**Insight**: Organic traffic delivers the best conversion rates, suggesting strong SEO performance. Social traffic underperforms and needs strategy review.

### 5. Trends Over Time
- Conversion rates are **improving** month-over-month
- Bounce rates are **decreasing** for Product A
- Traffic volume is **growing steadily**

## Business Recommendations

### Immediate Actions
1. **Increase Organic Traffic Investment**
   - Best conversion rates
   - Lower cost per acquisition
   - Invest in SEO and content marketing

2. **Optimize Desktop Experience**
   - Desktop users convert best
   - Ensure site speed and UX are optimal
   - Consider desktop-first design approach

3. **Improve Mobile Conversion**
   - Mobile is largest traffic source
   - Test mobile checkout process
   - Reduce mobile bounce rate

### Strategic Initiatives
4. **Replicate Product A Success**
   - Analyze what makes Product A successful
   - Apply learnings to Product B and C
   - A/B test similar approaches

5. **Review Social Media Strategy**
   - Lowest conversion rates
   - Reassess targeting and messaging
   - Consider reducing social ad spend

6. **Reduce Bounce Rates**
   - Average 49.7% bounce rate needs improvement
   - Test different headlines and CTAs
   - Improve page load speed

## Project Structure
```
03_python_data_cleaning/
├── website_traffic_data.csv          # Raw data
├── traffic_analysis.py                # Main analysis script
├── cleaned_traffic_data.csv           # Cleaned data (generated)
├── analysis_summary.txt               # Summary report (generated)
└── README.md                          # This file
```

## Skills Demonstrated
✅ **Data Cleaning**: Handling missing values, date parsing, feature engineering  
✅ **Data Analysis**: Aggregation, grouping, statistical analysis  
✅ **Business Intelligence**: Converting data into actionable insights  
✅ **Python Programming**: pandas, data manipulation, file I/O  
✅ **Communication**: Clear documentation and business recommendations  

## Next Steps for Expansion
- Create interactive visualizations with Plotly
- Build a dashboard with Streamlit or Dash
- Implement statistical testing for significance
- Add predictive modeling for conversion forecasting
- Automate reporting with scheduled Python scripts

## Contact
Created as part of my data analytics portfolio. This project demonstrates my ability to:
- Clean and prepare real-world data
- Perform exploratory data analysis
- Derive actionable business insights
- Communicate findings effectively

---

**Note**: This is a portfolio project with simulated but realistic data. The patterns and insights reflect real-world digital marketing scenarios.
