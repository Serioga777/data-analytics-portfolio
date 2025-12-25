# Job Market Analysis: Salary vs Stress Tolerance

## Project Overview

Analysis of the relationship between job stress tolerance requirements and average annual salaries across 10 professional careers. This project uses linear regression to understand whether higher stress positions command higher compensation.

## Key Findings

### Statistical Results
- **Correlation:** -0.774 (strong negative correlation)
- **R-squared:** 0.599 (model explains 59.9% of variance)
- **Regression equation:** Salary = 274.21 - 2.84 × Stress_Tolerance
- **P-value:** 0.009 (statistically significant)

### Insights

**Surprising Result:** Higher stress tolerance requirements are associated with LOWER salaries in this dataset.

- For every 1-point increase in stress tolerance requirement, salary decreases by $2,840
- Jobs requiring less stress tolerance (Political scientists, Law teachers) have the highest pay
- This challenges the common assumption that "high stress = high pay"

**Top Paying Careers:**
1. Political scientists: $102k (Stress: 60.1)
2. Law teachers: $100k (Stress: 62.8)
3. Optometrists: $98k (Stress: 65.5)

**Highest Stress Roles:**
- Dental hygienists: Stress 71.3, Salary $70k
- Urban planners: Stress 69.0, Salary $65k
- Engineers: Stress 69.5, Salary $92k

## Technical Approach

**Tools Used:**
- Python 3.13
- pandas for data manipulation
- statsmodels for regression analysis
- matplotlib for visualization
- scipy for statistical tests

**Methodology:**
1. Data cleaning and validation
2. Exploratory data analysis (correlation, descriptive stats)
3. OLS linear regression modeling
4. Residual analysis for model validation
5. Multi-panel visualization

## Data

**Source:** Job market statistics (10 professional careers)

**Variables:**
- Job title (categorical)
- Average annual salary in $1000s (continuous)
- Stress tolerance score 0-100 (continuous)

## Visualizations

### Main Dashboard
- Scatter plot with regression line
- Residual diagnostics
- Salary comparison by job
- Stress tolerance rankings

### Detailed Analysis
- Annotated scatter plot with all job titles
- Color-coded by salary level
- Confidence intervals shown

## Files

- `job_salary_analysis.py` - Main analysis script
- `job_salary_stress_data.csv` - Cleaned dataset
- `job_salary_stress_analysis.png` - 4-panel dashboard
- `job_salary_stress_detailed.png` - Detailed scatter plot

## Business Applications

**For Job Seekers:**
- Consider stress-to-pay ratio when evaluating offers
- High-paying roles don't always require high stress tolerance
- Academic/research positions offer good pay with lower stress

**For Employers:**
- High-stress roles may need premium compensation to attract talent
- Consider work-life balance as competitive advantage

**For Career Counseling:**
- Help clients understand trade-offs
- Not all high-paying careers are high-stress

## Limitations

- Small sample size (n=10)
- Cross-sectional data (point-in-time)
- Stress tolerance is subjective measure
- Results may not generalize to all industries

## Future Work

- Expand to larger job dataset
- Include additional factors (education, experience, location)
- Analyze by industry sector
- Time series analysis of trends
