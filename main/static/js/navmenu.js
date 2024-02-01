document.addEventListener('DOMContentLoaded', function () {
    // Add a click event listener to the button with class 'nav-button'
    var navButton = document.querySelector('.nav-button');
    var closeButton = document.querySelector('.close-button');
    var hiddenNavBar = document.querySelector('.hidden-navigation-bar');
   
    // open navigation bar
    navButton.addEventListener('click', function () {
        console.log('Open Button clicked!');
        hiddenNavBar.classList.toggle('nav-opened');
    });

    // close navigation bar
    closeButton.addEventListener('click', function () {
        console.log('Close Button clicked!');
        hiddenNavBar.classList.toggle('nav-opened');
    });
});