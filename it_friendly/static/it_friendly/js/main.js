window.onload = function () {

    $('header .hamburger').click(()=> {
        $('header nav').slideToggle()
        $('header .hamburger').toggleClass('active')
    })


     $('.container-slider').slick({
            dots: true,
            infinite: true,
            speed: 300,
            slidesToShow: 1,
            autoplay: true,
            autoplaySpeed: 4000,
            fade: true,
            arrows: false,
            cssEase: 'linear'
        });

    $('[data-modal]').click(function() {
    let cl = this.getAttribute('data-modal');
    let modal = document.getElementsByClassName(cl)[0];
    $(modal).slideToggle();

    $('.modal__window').not(modal).click(function(event) {
        event.stopPropagation();
    });
});


$('.close-button').click(() => {
    $('.modal__window').css('display', 'none');
});

}
