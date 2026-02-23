// Responsive Design - JavaScript for Hamburger Menu & Interactivity

// Get hamburger button and navigation menu
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');
const navLinks = document.querySelectorAll('.nav-menu a');

// Toggle menu on hamburger click
hamburger.addEventListener('click', function(e) {
    e.stopPropagation();
    navMenu.classList.toggle('active');
});

// Close menu when a nav link is clicked
navLinks.forEach(link => {
    link.addEventListener('click', function() {
        navMenu.classList.remove('active');
    });
});

// Close menu when clicking outside
document.addEventListener('click', function(event) {
    const isClickInsideNav = event.target.closest('.navbar');
    if (!isClickInsideNav && navMenu.classList.contains('active')) {
        navMenu.classList.remove('active');
    }
});

// Log responsive breakpoint info
function checkBreakpoint() {
    const width = window.innerWidth;
    let breakpoint = 'Desktop';
    
    if (width < 768) {
        breakpoint = 'Mobile';
    } else if (width < 1024) {
        breakpoint = 'Tablet';
    }
    
    console.log(`📱 Breakpoint: ${breakpoint} (${width}px)`);
}

// Check on load
window.addEventListener('load', checkBreakpoint);

// Check on resize
window.addEventListener('resize', function() {
    checkBreakpoint();
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
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

// Form validation
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('Thank you for your message! (Demo mode)');
        this.reset();
    });
}

// Log initial responsive info
console.log('%c=== RESPONSIVE DESIGN DEMO ===', 'color: #667eea; font-size: 16px; font-weight: bold;');
console.log('%cPercentage Width & Media Queries', 'color: #764ba2; font-size: 12px;');
console.log('%cMobile < 768px | Tablet 768-1023px | Desktop ≥ 1024px', 'color: #3498db; font-size: 11px;');
console.log('%cResize the window to see responsive changes', 'color: #27ae60; font-size: 11px;');
