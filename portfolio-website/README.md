# 🌐 Portfolio Website - Serghei Covalciuc

A modern, responsive portfolio website showcasing data analytics skills and projects.

![Portfolio Preview](https://img.shields.io/badge/Status-Live-brightgreen)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white)

## 🚀 Live Demo

**View Live:** [Your GitHub Pages URL]

## ✨ Features

### Design & UX
- 📱 **Fully Responsive** - Works perfectly on all devices (mobile, tablet, desktop)
- 🎨 **Modern UI** - Clean, professional design with gradient accents
- ⚡ **Fast Loading** - Optimized performance with lazy loading
- 🎭 **Smooth Animations** - AOS (Animate On Scroll) library
- 🌊 **Smooth Scrolling** - Enhanced navigation experience

### Sections
1. **Hero Section** - Eye-catching introduction with typing animation
2. **Stats Section** - Animated counters showing key metrics
3. **About Section** - Personal information and skills overview
4. **Projects Section** - 3 featured data analytics projects
5. **Skills Section** - Categorized technical skills
6. **Contact Section** - Functional contact form
7. **Footer** - Social links and copyright

### Interactive Features
- ✅ Mobile-friendly navigation menu
- ✅ Typing animation for skills
- ✅ Counter animations for statistics
- ✅ Hover effects on cards and buttons
- ✅ Form validation
- ✅ Scroll-to-top button
- ✅ Active nav link highlighting
- ✅ Keyboard shortcuts (h, p, c)

## 🛠️ Technologies Used

### Core
- **HTML5** - Semantic markup
- **CSS3** - Modern styling
- **JavaScript (ES6+)** - Interactive functionality
- **Tailwind CSS** - Utility-first CSS framework

### Libraries & Tools
- **AOS** - Animate On Scroll library
- **Font Awesome** - Icon library
- **Google Fonts** - Inter & Poppins fonts

## 📂 Project Structure

```
portfolio-website/
├── index.html              # Main HTML file
├── js/
│   └── main.js            # JavaScript functionality
├── assets/                 # Images and icons (optional)
├── DESIGN_SKETCH.md       # Design documentation
└── README.md              # This file
```

## 🎨 Color Palette

```css
--navy: #1e3a8a      /* Primary dark blue */
--sky: #0ea5e9       /* Bright blue accent */
--emerald: #10b981   /* Success green */
--purple: #8b5cf6    /* Purple accent */
--orange: #f59e0b    /* Orange accent */
```

## 🚀 Getting Started

### Option 1: Open Locally

1. Clone or download this repository
2. Open `index.html` in your browser
3. That's it! No build process required.

### Option 2: Deploy to GitHub Pages

1. Create a new repository on GitHub (e.g., `portfolio-website`)
2. Upload all files to the repository
3. Go to Settings → Pages
4. Select `main` branch as source
5. Your site will be live at: `https://yourusername.github.io/portfolio-website`

### Option 3: Use VS Code Live Server

1. Open folder in VS Code
2. Install "Live Server" extension
3. Right-click `index.html` → "Open with Live Server"
4. Automatically opens in browser with live reload

## 📱 Responsive Breakpoints

- **Mobile**: < 640px
- **Tablet**: 640px - 1024px
- **Desktop**: > 1024px
- **Large Desktop**: > 1280px

## ⚡ Performance

- Fast initial load (< 2 seconds)
- Lazy loading for images
- Minified CDN resources
- Optimized animations
- Mobile-first approach

## 🔧 Customization

### Change Colors

Edit the CSS variables in `index.html`:

```css
:root {
    --navy: #1e3a8a;
    --sky: #0ea5e9;
    /* etc... */
}
```

### Update Content

1. **Personal Info**: Update name, email, phone in HTML
2. **Projects**: Modify project cards in Projects section
3. **Skills**: Edit skills list in Skills section
4. **Social Links**: Update href attributes for social icons

### Add More Sections

Follow the existing section structure:

```html
<section id="new-section" class="py-20 bg-slate-900">
    <div class="max-w-7xl mx-auto px-4">
        <!-- Your content -->
    </div>
</section>
```

## 📧 Contact Form Setup

The contact form currently shows a success message (demo mode).

To integrate with a real email service:

### Option 1: EmailJS (Recommended)

1. Sign up at [EmailJS.com](https://www.emailjs.com/)
2. Create email template
3. Uncomment and modify the EmailJS code in `main.js`
4. Add your service ID and template ID

### Option 2: Formspree

1. Sign up at [Formspree.io](https://formspree.io/)
2. Change form action: `<form action="https://formspree.io/f/YOUR_ID">`

### Option 3: Custom Backend

Create your own backend API and update the fetch URL in `main.js`

## ♿ Accessibility

- Semantic HTML5 elements
- ARIA labels where needed
- Keyboard navigation support
- High contrast ratios
- Screen reader friendly

## 📊 SEO Features

- Meta tags for description and keywords
- Open Graph tags for social sharing
- Semantic HTML structure
- Clean URLs
- Fast loading times

## 🎯 Browser Support

- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)
- ✅ Mobile browsers

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Serghei Covalciuc**

- GitHub: [@Serioga777](https://github.com/Serioga777)
- LinkedIn: [sergheicovalciuc93](https://linkedin.com/in/sergheicovalciuc93)
- Email: sergheicovalciuc0000@gmail.com
- Portfolio: [github.com/Serioga777/data-analytics-portfolio](https://github.com/Serioga777/data-analytics-portfolio)

## 🙏 Acknowledgments

- **Tailwind CSS** - For the utility-first CSS framework
- **AOS** - For smooth scroll animations
- **Font Awesome** - For beautiful icons
- **Google Fonts** - For Inter and Poppins fonts

## 📈 Future Enhancements

- [ ] Dark/Light theme toggle
- [ ] Blog section
- [ ] Project filtering by technology
- [ ] Multi-language support (EN/RO/RU)
- [ ] Testimonials slider
- [ ] PWA (Progressive Web App) features
- [ ] Analytics integration

## 🐛 Bug Reports

If you find any bugs, please open an issue on GitHub or contact me directly.

## 💡 Contributing

Suggestions and improvements are welcome! Feel free to fork and create a pull request.

---

**Made with ❤️ using HTML, CSS, JavaScript & Tailwind CSS**

⭐ Star this repo if you found it helpful!
