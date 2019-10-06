/*** Enable hover on dropdown menu. ***/
$('.dropdown-hoverable').hover(function(){
    $(this).children('[data-toggle="dropdown"]').click();
}, function(){
    $(this).children('[data-toggle="dropdown"]').click();
});
