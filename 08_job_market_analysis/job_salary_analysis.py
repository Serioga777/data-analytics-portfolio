import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm

# Extract and clean data from academic project
print("Loading job salary and stress data...")
df = pd.read_excel('9408_Serghei_Covalciuc_BSU_MD_Test_1_to_8_Cohort_7_Resubmission_55231_656397023.xlsx', 
                   sheet_name='Test 8')

# Clean the data - keep only the first 10 valid rows
df_clean = df.iloc[:10, [0, 1, 2]].copy()
df_clean.columns = ['Job', 'Salary', 'Stress_Tolerance']
df_clean = df_clean.dropna()

# Convert to proper types
df_clean['Salary'] = pd.to_numeric(df_clean['Salary'])
df_clean['Stress_Tolerance'] = pd.to_numeric(df_clean['Stress_Tolerance'])

# Save cleaned data
df_clean.to_csv('job_salary_stress_data.csv', index=False)

print(f"\nCleaned dataset: {df_clean.shape[0]} jobs")
print("\nSample data:")
print(df_clean)

print("\n" + "="*80)
print("JOB MARKET ANALYSIS: SALARY VS STRESS TOLERANCE")
print("="*80)

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df_clean[['Salary', 'Stress_Tolerance']].describe())

# Correlation
correlation = df_clean['Salary'].corr(df_clean['Stress_Tolerance'])
print(f"\nCorrelation coefficient: {correlation:.4f}")

# Linear regression
X = df_clean['Stress_Tolerance'].values.reshape(-1, 1)
y = df_clean['Salary'].values

# Using statsmodels for detailed stats
X_sm = sm.add_constant(X)
model = sm.OLS(y, X_sm)
results = model.fit()

print("\n" + "="*80)
print("REGRESSION RESULTS")
print("="*80)
print(results.summary())

# Extract coefficients
intercept = results.params[0]
slope = results.params[1]
r_squared = results.rsquared

print(f"\nRegression Equation:")
print(f"Salary = {intercept:.2f} + {slope:.2f} × Stress_Tolerance")
print(f"R² = {r_squared:.4f}")

# Create professional visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Job Market Analysis: Salary vs Stress Tolerance', fontsize=16, fontweight='bold')

# 1. Scatter plot with regression line
axes[0, 0].scatter(df_clean['Stress_Tolerance'], df_clean['Salary'], 
                   alpha=0.7, s=100, color='#2E86AB', edgecolor='black', linewidth=1.5)
axes[0, 0].plot(df_clean['Stress_Tolerance'], results.fittedvalues, 
                color='#A23B72', linewidth=2.5, label=f'y = {intercept:.1f} + {slope:.1f}x')
axes[0, 0].set_xlabel('Stress Tolerance', fontsize=11, fontweight='bold')
axes[0, 0].set_ylabel('Average Annual Salary ($1000s)', fontsize=11, fontweight='bold')
axes[0, 0].set_title(f'Salary vs Stress Tolerance\nR² = {r_squared:.4f}', fontsize=12, fontweight='bold')
axes[0, 0].legend(fontsize=10)
axes[0, 0].grid(True, alpha=0.3)

# 2. Residual plot
residuals = results.resid
axes[0, 1].scatter(results.fittedvalues, residuals, alpha=0.7, s=100, 
                   color='#F18F01', edgecolor='black', linewidth=1.5)
axes[0, 1].axhline(y=0, color='red', linestyle='--', linewidth=2)
axes[0, 1].set_xlabel('Fitted Values', fontsize=11, fontweight='bold')
axes[0, 1].set_ylabel('Residuals', fontsize=11, fontweight='bold')
axes[0, 1].set_title('Residual Plot', fontsize=12, fontweight='bold')
axes[0, 1].grid(True, alpha=0.3)

# 3. Bar chart of salaries
df_sorted = df_clean.sort_values('Salary', ascending=True)
colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(df_sorted)))
axes[1, 0].barh(df_sorted['Job'], df_sorted['Salary'], color=colors, edgecolor='black', linewidth=1)
axes[1, 0].set_xlabel('Average Annual Salary ($1000s)', fontsize=11, fontweight='bold')
axes[1, 0].set_title('Average Salaries by Job Title', fontsize=12, fontweight='bold')
axes[1, 0].grid(axis='x', alpha=0.3)

# 4. Stress tolerance comparison
df_sorted_stress = df_clean.sort_values('Stress_Tolerance', ascending=True)
colors2 = plt.cm.coolwarm(np.linspace(0.2, 0.8, len(df_sorted_stress)))
axes[1, 1].barh(df_sorted_stress['Job'], df_sorted_stress['Stress_Tolerance'], 
                color=colors2, edgecolor='black', linewidth=1)
axes[1, 1].set_xlabel('Stress Tolerance Score', fontsize=11, fontweight='bold')
axes[1, 1].set_title('Stress Tolerance by Job Title', fontsize=12, fontweight='bold')
axes[1, 1].grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig('job_salary_stress_analysis.png', dpi=300, bbox_inches='tight')
print("\n✓ Visualization saved: job_salary_stress_analysis.png")

# Create a second detailed plot
fig2, ax = plt.subplots(figsize=(12, 8))

# Enhanced scatter plot with labels
scatter = ax.scatter(df_clean['Stress_Tolerance'], df_clean['Salary'], 
                     s=200, alpha=0.6, c=df_clean['Salary'], cmap='RdYlGn',
                     edgecolor='black', linewidth=2)

# Add regression line
ax.plot(df_clean['Stress_Tolerance'], results.fittedvalues, 
        color='darkblue', linewidth=3, label=f'Linear fit: R² = {r_squared:.3f}', linestyle='--')

# Add labels for each point
for idx, row in df_clean.iterrows():
    ax.annotate(row['Job'], 
                (row['Stress_Tolerance'], row['Salary']),
                xytext=(5, 5), textcoords='offset points',
                fontsize=9, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3))

ax.set_xlabel('Stress Tolerance Score', fontsize=13, fontweight='bold')
ax.set_ylabel('Average Annual Salary ($1000s)', fontsize=13, fontweight='bold')
ax.set_title('Career Analysis: Does Higher Stress Mean Higher Pay?', 
             fontsize=15, fontweight='bold', pad=20)
ax.legend(fontsize=12, loc='best')
ax.grid(True, alpha=0.3, linestyle='--')

# Add colorbar
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Salary Level', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('job_salary_stress_detailed.png', dpi=300, bbox_inches='tight')
print("✓ Detailed visualization saved: job_salary_stress_detailed.png")

# Generate insights report
print("\n" + "="*80)
print("KEY INSIGHTS")
print("="*80)

print("\n1. Relationship Analysis:")
if correlation > 0:
    print(f"   - Positive correlation ({correlation:.4f}) between stress tolerance and salary")
    print(f"   - Jobs requiring higher stress tolerance tend to pay more")
else:
    print(f"   - Negative correlation ({correlation:.4f}) between stress tolerance and salary")
    
print(f"\n2. Regression Model:")
print(f"   - For every 1-point increase in stress tolerance, salary increases by ${slope:.2f}k")
print(f"   - Model explains {r_squared*100:.1f}% of salary variance (R² = {r_squared:.4f})")

print(f"\n3. Top Paying Jobs:")
top_3 = df_clean.nlargest(3, 'Salary')[['Job', 'Salary', 'Stress_Tolerance']]
for idx, row in top_3.iterrows():
    print(f"   - {row['Job']}: ${row['Salary']}k (Stress: {row['Stress_Tolerance']})")

print(f"\n4. Lowest Stress Jobs:")
low_stress = df_clean.nsmallest(3, 'Stress_Tolerance')[['Job', 'Salary', 'Stress_Tolerance']]
for idx, row in low_stress.iterrows():
    print(f"   - {row['Job']}: ${row['Salary']}k (Stress: {row['Stress_Tolerance']})")

print("\n" + "="*80)
print("ANALYSIS COMPLETE")
print("="*80)
