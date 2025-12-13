# 🚀 QUICK GITHUB UPLOAD - TWO OPTIONS

## Option 1: Automated Upload (Easiest) ⭐

**Step 1:** Create repository on GitHub
- Go to: https://github.com/new
- Name: `data-analytics-portfolio`
- Description: `Data Analytics Portfolio - Excel, SQL, Python projects`
- Make it **PUBLIC**
- **DON'T** check "Add a README file"
- Click "Create repository"

**Step 2:** Run the upload script
```powershell
cd "c:\Users\deathy\Documents\multi agent test"
.\upload_to_github.ps1
```

**Step 3:** Enter your info when prompted
- GitHub username
- Repository name (or press Enter for default)
- Confirm repository is created
- Enter credentials (use Personal Access Token as password)

**Done!** ✅

---

## Option 2: Manual Upload via GitHub Website

**Step 1:** Create repository (same as above)

**Step 2:** Upload files
1. In your new repository, click "uploading an existing file"
2. Drag and drop the entire `data_analytics_portfolio` folder
3. Add commit message: "Add data analytics portfolio projects"
4. Click "Commit changes"

**Done!** ✅

---

## 🔑 Creating a Personal Access Token

If you don't have a Personal Access Token:

1. Go to: https://github.com/settings/tokens/new
2. Note: "Portfolio Upload"
3. Expiration: 90 days
4. Select scope: ✅ **repo** (full control)
5. Click "Generate token"
6. **COPY THE TOKEN** immediately (you won't see it again!)
7. Use this as your password when pushing

---

## ✅ After Upload Checklist

- [ ] Repository is PUBLIC
- [ ] All files uploaded successfully
- [ ] README displays correctly
- [ ] Add repository description
- [ ] Add topics: `data-analytics` `portfolio` `excel` `sql` `python`
- [ ] Pin repository to your profile
- [ ] Add link to CV
- [ ] Add link to LinkedIn Featured section

---

## 📎 Your Portfolio Link

After upload, share this link:
```
https://github.com/YOUR_USERNAME/data-analytics-portfolio
```

**Add this link to:**
✅ CV/Resume  
✅ LinkedIn Featured section  
✅ Job applications  
✅ Email signature  

---

## 🆘 Troubleshooting

**"Permission denied"**
→ Use Personal Access Token, not password

**"Repository not found"**
→ Make sure repository exists on GitHub

**"Git not recognized"**
→ Git is already installed, restart PowerShell

**Script won't run**
→ Run: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass`

---

## 📞 Need Help?

Check the full guide:
- `GitHub_Upload_Guide.md` - Detailed instructions
- `upload_to_github.ps1` - Automated upload script

---

**Estimated Time:** 10-15 minutes

**You've got this!** 🚀
