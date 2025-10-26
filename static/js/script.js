// THEME TOGGLE - SIMPLE AND WORKING
document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.getElementById('theme-toggle');
    const html = document.documentElement;
    
    // Load saved theme
    if (localStorage.getItem('theme') === 'light') {
        html.classList.add('light-theme');
    }
    
    // Toggle on click
    if (toggle) {
        toggle.addEventListener('click', function() {
            this.classList.add('rotating');
            html.classList.toggle('light-theme');
            localStorage.setItem('theme', html.classList.contains('light-theme') ? 'light' : 'dark');
            setTimeout(() => this.classList.remove('rotating'), 500);
        });
    }
});