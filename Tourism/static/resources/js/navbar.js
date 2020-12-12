$(window).on('scroll', function () {
    if ($(window).scrollTop()) {
        $('#navbar').addClass('effectbg')
    }
    else {
        $('#navbar').removeClass('effectbg')
    }
})