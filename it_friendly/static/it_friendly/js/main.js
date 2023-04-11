window.onload = function () {
    // BURGER
    $('header .hamburger').click(()=> {
        $('header nav').slideToggle()
        $('header .hamburger').toggleClass('active')
    })

        //Slider
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

    //Modal
    // $('.ask-question .choose-course').click(() => {
    //     $('.askquestion').slideToggle()
    //     }
    // )
/*
    $('[data-modal]').click(function() {
        let cl = this.getAttribute('data-modal')
        let modal = document.getElementsByClassName(cl)[0]
        $(modal).slideToggle()
    })

    $('.modal__window').click(() => {
        $('.modal__window').css('display','none')
        }
    )
    $('.close-button').click(() => {
            $('.modal__window').css('display','none')
        }
    )*/
    $('[data-modal]').click(function() {
    let cl = this.getAttribute('data-modal');
    let modal = document.getElementsByClassName(cl)[0];
    $(modal).slideToggle();

    // відміна події кліку на інших елементах модального вікна
    $('.modal__window').not(modal).click(function(event) {
        event.stopPropagation();
    });
});

// закриття модального вікна при кліку на кнопку "Закрити"
$('.close-button').click(() => {
    $('.modal__window').css('display', 'none');
});

}