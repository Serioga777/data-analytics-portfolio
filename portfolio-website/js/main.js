// Initialize AOS (Animate On Scroll)
AOS.init({
    duration: 1000,
    once: true,
    offset: 100
});

// Mobile Menu Toggle
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

mobileMenuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});

// Close mobile menu when clicking on a link
const mobileMenuLinks = mobileMenu.querySelectorAll('a');
mobileMenuLinks.forEach(link => {
    link.addEventListener('click', () => {
        mobileMenu.classList.add('hidden');
    });
});

// Typing Animation
const typedTextElement = document.getElementById('typed-text');
const textArray = ['Excel Expert', 'SQL Developer', 'Python Analyst', 'Data Enthusiast'];
let textArrayIndex = 0;
let charIndex = 0;
let isDeleting = false;
let typingDelay = 200;
let erasingDelay = 100;
let newTextDelay = 2000;

function type() {
    if (textArrayIndex === textArray.length) {
        textArrayIndex = 0;
    }
    
    const currentText = textArray[textArrayIndex];
    
    if (isDeleting) {
        typedTextElement.textContent = currentText.substring(0, charIndex - 1);
        charIndex--;
    } else {
        typedTextElement.textContent = currentText.substring(0, charIndex + 1);
        charIndex++;
    }
    
    if (!isDeleting && charIndex === currentText.length) {
        isDeleting = true;
        typingDelay = newTextDelay;
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        textArrayIndex++;
        typingDelay = 500;
    } else {
        typingDelay = isDeleting ? erasingDelay : 200;
    }
    
    setTimeout(type, typingDelay);
}

// Start typing animation when page loads
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(type, newTextDelay + 250);
});

// Animated Counter for Stats
function animateCounter(element) {
    const target = parseInt(element.getAttribute('data-target'));
    const increment = target / 100;
    let current = 0;
    
    const updateCounter = () => {
        current += increment;
        if (current < target) {
            element.textContent = Math.ceil(current);
            setTimeout(updateCounter, 20);
        } else {
            element.textContent = target;
        }
    };
    
    updateCounter();
}

// Trigger counters when in viewport
const observerOptions = {
    threshold: 0.5,
    rootMargin: '0px'
};

const observerCallback = (entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const counters = entry.target.querySelectorAll('.counter');
            counters.forEach(counter => {
                if (!counter.classList.contains('counted')) {
                    animateCounter(counter);
                    counter.classList.add('counted');
                }
            });
            observer.unobserve(entry.target);
        }
    });
};

const observer = new IntersectionObserver(observerCallback, observerOptions);
const statsSection = document.querySelector('.grid.grid-cols-2.md\\:grid-cols-4');
if (statsSection) {
    observer.observe(statsSection);
}

// Smooth Scrolling for Navigation Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Active Navigation Link on Scroll
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('nav a[href^="#"]');

function highlightNavigation() {
    const scrollPosition = window.scrollY + 100;
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        const sectionId = section.getAttribute('id');
        
        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
            navLinks.forEach(link => {
                link.classList.remove('text-sky-400');
                if (link.getAttribute('href') === `#${sectionId}`) {
                    link.classList.add('text-sky-400');
                }
            });
        }
    });
}

window.addEventListener('scroll', highlightNavigation);

// Contact Form Handling
const contactForm = document.getElementById('contact-form');
const formMessage = document.getElementById('form-message');

contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
    
    // Show loading state
    const submitBtn = contactForm.querySelector('button[type="submit"]');
    const originalBtnText = submitBtn.innerHTML;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i>Sending...';
    submitBtn.disabled = true;
    
    // Simulate form submission (replace with actual email service)
    setTimeout(() => {
        formMessage.classList.remove('hidden');
        formMessage.className = 'mt-4 text-center p-4 bg-emerald-500 bg-opacity-20 border border-emerald-500 rounded-lg text-emerald-400';
        formMessage.innerHTML = '<i class="fas fa-check-circle mr-2"></i>Message sent successfully! I\'ll get back to you soon.';
        
        // Reset form
        contactForm.reset();
        
        // Reset button
        submitBtn.innerHTML = originalBtnText;
        submitBtn.disabled = false;
        
        // Hide message after 5 seconds
        setTimeout(() => {
            formMessage.classList.add('hidden');
        }, 5000);
    }, 1500);
    
    /* 
    // To integrate with EmailJS or similar service:
    try {
        const response = await fetch('YOUR_EMAIL_API_ENDPOINT', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, email, message })
        });
        
        if (response.ok) {
            // Success message
            formMessage.classList.remove('hidden');
            formMessage.className = 'mt-4 text-center p-4 bg-emerald-500 bg-opacity-20 border border-emerald-500 rounded-lg text-emerald-400';
            formMessage.innerHTML = '<i class="fas fa-check-circle mr-2"></i>Message sent successfully!';
            contactForm.reset();
        } else {
            throw new Error('Failed to send');
        }
    } catch (error) {
        // Error message
        formMessage.classList.remove('hidden');
        formMessage.className = 'mt-4 text-center p-4 bg-red-500 bg-opacity-20 border border-red-500 rounded-lg text-red-400';
        formMessage.innerHTML = '<i class="fas fa-exclamation-circle mr-2"></i>Failed to send message. Please try again.';
    } finally {
        submitBtn.innerHTML = originalBtnText;
        submitBtn.disabled = false;
    }
    */
});

// Form Input Validation Styling
const formInputs = contactForm.querySelectorAll('input, textarea');
formInputs.forEach(input => {
    input.addEventListener('blur', () => {
        if (input.value.trim() !== '') {
            input.classList.add('border-emerald-400');
            input.classList.remove('border-red-400');
        }
    });
    
    input.addEventListener('invalid', (e) => {
        e.preventDefault();
        input.classList.add('border-red-400');
        input.classList.remove('border-emerald-400');
    });
    
    input.addEventListener('input', () => {
        if (input.validity.valid) {
            input.classList.remove('border-red-400');
        }
    });
});

// Navbar Background on Scroll
const navbar = document.querySelector('nav');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('bg-slate-900', 'bg-opacity-95');
        navbar.classList.remove('glass');
    } else {
        navbar.classList.remove('bg-slate-900', 'bg-opacity-95');
        navbar.classList.add('glass');
    }
});

// Add parallax effect to hero section (optional)
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const heroSection = document.querySelector('#home');
    if (heroSection) {
        heroSection.style.transform = `translateY(${scrolled * 0.5}px)`;
    }
});

// Lazy load images if any
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    const images = document.querySelectorAll('img.lazy');
    images.forEach(img => imageObserver.observe(img));
}

// Console Easter Egg
console.log('%c👋 Hello fellow developer!', 'color: #0ea5e9; font-size: 20px; font-weight: bold;');
console.log('%c🚀 Thanks for checking out my portfolio!', 'color: #8b5cf6; font-size: 16px;');
console.log('%c📧 Let\'s connect: sergheicovalciuc0000@gmail.com', 'color: #10b981; font-size: 14px;');
console.log('%c💻 GitHub: https://github.com/Serioga777', 'color: #f59e0b; font-size: 14px;');

// Add keyboard shortcuts
document.addEventListener('keydown', (e) => {
    // Press 'h' to go to home
    if (e.key === 'h' && !e.ctrlKey && !e.metaKey) {
        if (document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
            document.querySelector('#home').scrollIntoView({ behavior: 'smooth' });
        }
    }
    
    // Press 'p' to go to projects
    if (e.key === 'p' && !e.ctrlKey && !e.metaKey) {
        if (document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
            document.querySelector('#projects').scrollIntoView({ behavior: 'smooth' });
        }
    }
    
    // Press 'c' to go to contact
    if (e.key === 'c' && !e.ctrlKey && !e.metaKey) {
        if (document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
            document.querySelector('#contact').scrollIntoView({ behavior: 'smooth' });
        }
    }
});

// Show a "scroll to top" button when scrolled down
const scrollToTopBtn = document.createElement('button');
scrollToTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
scrollToTopBtn.className = 'fixed bottom-8 right-8 bg-sky-500 hover:bg-sky-600 text-white w-12 h-12 rounded-full shadow-lg transition transform hover:scale-110 opacity-0 pointer-events-none';
scrollToTopBtn.id = 'scroll-to-top';
document.body.appendChild(scrollToTopBtn);

window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        scrollToTopBtn.style.opacity = '1';
        scrollToTopBtn.style.pointerEvents = 'auto';
    } else {
        scrollToTopBtn.style.opacity = '0';
        scrollToTopBtn.style.pointerEvents = 'none';
    }
});

scrollToTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Performance monitoring
window.addEventListener('load', () => {
    const loadTime = window.performance.timing.domContentLoadedEventEnd - window.performance.timing.navigationStart;
    console.log(`%c⚡ Page loaded in ${loadTime}ms`, 'color: #10b981; font-weight: bold;');
});
