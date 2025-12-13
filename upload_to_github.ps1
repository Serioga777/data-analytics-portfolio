# GitHub Upload Script for Your Portfolio
# This script will help you upload your data analytics portfolio to GitHub

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  DATA ANALYTICS PORTFOLIO UPLOADER" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Get GitHub username
Write-Host "Step 1: GitHub Account Setup" -ForegroundColor Yellow
Write-Host ""
$username = Read-Host "Enter your GitHub username"
Write-Host ""

# Step 2: Repository name
Write-Host "Step 2: Repository Name" -ForegroundColor Yellow
Write-Host "Recommended: data-analytics-portfolio" -ForegroundColor Gray
$repoName = Read-Host "Enter repository name (press Enter for default)"
if ([string]::IsNullOrWhiteSpace($repoName)) {
    $repoName = "data-analytics-portfolio"
}
Write-Host ""

# Display what will happen
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  READY TO UPLOAD" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Repository URL: https://github.com/$username/$repoName" -ForegroundColor Green
Write-Host ""
Write-Host "Files to upload:" -ForegroundColor Yellow
Write-Host "  ✓ data_analytics_portfolio/" -ForegroundColor Green
Write-Host "    ├── README.md (Portfolio overview)" -ForegroundColor Gray
Write-Host "    ├── PORTFOLIO_SUMMARY.md" -ForegroundColor Gray
Write-Host "    ├── 01_excel_sales_dashboard/" -ForegroundColor Gray
Write-Host "    │   ├── sales_data_2024.csv" -ForegroundColor Gray
Write-Host "    │   └── README.md" -ForegroundColor Gray
Write-Host "    ├── 02_sql_customer_analysis/" -ForegroundColor Gray
Write-Host "    │   ├── database_setup.sql" -ForegroundColor Gray
Write-Host "    │   ├── analysis_queries.sql" -ForegroundColor Gray
Write-Host "    │   └── README.md" -ForegroundColor Gray
Write-Host "    └── 03_python_data_cleaning/" -ForegroundColor Gray
Write-Host "        ├── website_traffic_data.csv" -ForegroundColor Gray
Write-Host "        ├── traffic_analysis.py" -ForegroundColor Gray
Write-Host "        └── README.md" -ForegroundColor Gray
Write-Host ""

# Confirm
Write-Host "IMPORTANT: Before continuing, make sure you have:" -ForegroundColor Red
Write-Host "  1. Created the repository on GitHub.com" -ForegroundColor Yellow
Write-Host "     (Go to GitHub.com → '+' → New repository)" -ForegroundColor Gray
Write-Host "  2. Named it: $repoName" -ForegroundColor Yellow
Write-Host "  3. Made it PUBLIC (so employers can see it)" -ForegroundColor Yellow
Write-Host "  4. DO NOT initialize with README (we have our own)" -ForegroundColor Yellow
Write-Host ""

$continue = Read-Host "Have you created the repository on GitHub? (yes/no)"
if ($continue -ne "yes") {
    Write-Host ""
    Write-Host "Please create the repository on GitHub first:" -ForegroundColor Red
    Write-Host "  1. Go to https://github.com/new" -ForegroundColor Yellow
    Write-Host "  2. Repository name: $repoName" -ForegroundColor Yellow
    Write-Host "  3. Description: Data Analytics Portfolio - Excel, SQL, Python projects" -ForegroundColor Yellow
    Write-Host "  4. Make it PUBLIC" -ForegroundColor Yellow
    Write-Host "  5. DO NOT check 'Add a README file'" -ForegroundColor Yellow
    Write-Host "  6. Click 'Create repository'" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Then run this script again!" -ForegroundColor Cyan
    Write-Host ""
    exit
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  STARTING UPLOAD..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Navigate to the portfolio directory
$portfolioPath = "c:\Users\deathy\Documents\multi agent test\data_analytics_portfolio"
Set-Location -Path $portfolioPath

# Initialize git if not already initialized
if (-not (Test-Path ".git")) {
    Write-Host "[1/7] Initializing Git repository..." -ForegroundColor Yellow
    git init
    Write-Host "      ✓ Git initialized" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host "[1/7] Git already initialized" -ForegroundColor Green
    Write-Host ""
}

# Configure git user (if not set)
Write-Host "[2/7] Configuring Git..." -ForegroundColor Yellow
$gitUser = git config user.name
if ([string]::IsNullOrWhiteSpace($gitUser)) {
    $name = Read-Host "      Enter your name for Git commits"
    git config user.name "$name"
}
$gitEmail = git config user.email
if ([string]::IsNullOrWhiteSpace($gitEmail)) {
    $email = Read-Host "      Enter your email for Git commits"
    git config user.email "$email"
}
Write-Host "      ✓ Git configured" -ForegroundColor Green
Write-Host ""

# Add all files
Write-Host "[3/7] Adding all portfolio files..." -ForegroundColor Yellow
git add .
Write-Host "      ✓ Files added" -ForegroundColor Green
Write-Host ""

# Commit
Write-Host "[4/7] Creating commit..." -ForegroundColor Yellow
git commit -m "Add data analytics portfolio with Excel, SQL, and Python projects"
Write-Host "      ✓ Files committed" -ForegroundColor Green
Write-Host ""

# Add remote
Write-Host "[5/7] Connecting to GitHub..." -ForegroundColor Yellow
$remoteUrl = "https://github.com/$username/$repoName.git"
try {
    git remote add origin $remoteUrl 2>$null
    Write-Host "      ✓ Connected to GitHub repository" -ForegroundColor Green
} catch {
    # Remote might already exist
    git remote set-url origin $remoteUrl
    Write-Host "      ✓ Updated GitHub repository URL" -ForegroundColor Green
}
Write-Host ""

# Rename branch to main
Write-Host "[6/7] Setting up main branch..." -ForegroundColor Yellow
git branch -M main
Write-Host "      ✓ Branch configured" -ForegroundColor Green
Write-Host ""

# Push
Write-Host "[7/7] Uploading to GitHub..." -ForegroundColor Yellow
Write-Host ""
Write-Host "      You'll be prompted for your GitHub credentials:" -ForegroundColor Cyan
Write-Host "      Username: $username" -ForegroundColor Gray
Write-Host "      Password: Use your Personal Access Token (NOT your regular password)" -ForegroundColor Gray
Write-Host ""
Write-Host "      Don't have a token? Create one at:" -ForegroundColor Yellow
Write-Host "      https://github.com/settings/tokens/new" -ForegroundColor Blue
Write-Host "      (Check the 'repo' scope and copy the token)" -ForegroundColor Gray
Write-Host ""

git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "  ✓ SUCCESS! PORTFOLIO UPLOADED!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Your portfolio is now live at:" -ForegroundColor Cyan
    Write-Host "https://github.com/$username/$repoName" -ForegroundColor Blue
    Write-Host ""
    Write-Host "Next Steps:" -ForegroundColor Yellow
    Write-Host "  1. Visit your repository to verify upload" -ForegroundColor White
    Write-Host "  2. Add repository description and topics on GitHub" -ForegroundColor White
    Write-Host "  3. Pin the repository to your GitHub profile" -ForegroundColor White
    Write-Host "  4. Add the link to your CV and LinkedIn" -ForegroundColor White
    Write-Host ""
    Write-Host "Share this link with employers:" -ForegroundColor Cyan
    Write-Host "https://github.com/$username/$repoName" -ForegroundColor Blue
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "  UPLOAD FAILED" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Common issues:" -ForegroundColor Yellow
    Write-Host "  1. Wrong credentials - Make sure to use Personal Access Token" -ForegroundColor White
    Write-Host "  2. Repository doesn't exist - Create it on GitHub first" -ForegroundColor White
    Write-Host "  3. Repository name mismatch - Check spelling" -ForegroundColor White
    Write-Host ""
    Write-Host "Try running the script again or upload manually via GitHub website" -ForegroundColor Cyan
    Write-Host ""
}

# Return to original directory
Set-Location -Path "c:\Users\deathy\Documents\multi agent test"
