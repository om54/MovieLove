const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navlinks');

hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');

    // Optional: Switch icon from bars to an 'X'
    const icon = hamburger.querySelector('i');
    icon.classList.toggle('fa-bars');
    icon.classList.toggle('fa-xmark');
});


const searchIcon = document.getElementById("searchicon");
const searchBar = document.getElementById("searchbar");
const searchOverlay = document.getElementById("search-overlay");

searchIcon.addEventListener('click', () => {
    const isOpen = searchBar.classList.toggle('active');
    searchOverlay.classList.toggle('active', isOpen);
    document.body.classList.toggle('search-open', isOpen);

    searchIcon.classList.toggle('fa-search');
    searchIcon.classList.toggle('fa-xmark');
})

searchOverlay.addEventListener('click', closeWindow);

function closeWindow() {
    searchBar.classList.remove('active');
    searchOverlay.classList.remove('active');
    document.body.classList.remove('search-open');
    searchIcon.classList.remove('fa-xmark');
    searchIcon.classList.add('fa-search');
}