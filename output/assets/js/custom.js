/*** Enable hover on dropdown menu. ***/
$('ul.navbar-nav li.dropdown').hover(function () {
    $(this).find('.dropdown-menu').stop(true, true).delay(50).fadeIn(100);
}, function () {
    $(this).find('.dropdown-menu').stop(true, true).delay(50).fadeOut(100);
});