$('.header__slider').each(function(){
    $(this).slick({
        dots: true, 
        arrows: true,
    });
 });



 $('.slider__slick').each(function(){
    $(this).slick({
        dots: true, 
        slidesToShow: 5,
        arrows: true,
        slidesToScroll: 4,
    });
 });



 $(document).ready(function(){
    $('.menu__slider__small').slick({

        dots: false, 
        slidesToShow: 3,
        arrows: true,
        vertical: true,
        slidesToScroll: 1,
        centerMode: true,
        focusOnSelect: true,
        asNavFor: '.menu__slider__big, #slider-6',
        infinite: false,
    });
 });


 $(document).ready(function(){
    $('.menu__slider__big').slick({

        dots: false, 
        arrows: true,
        asNavFor: '#slider-6, .menu__slider__small',
        infinite: false,

    });
 });




 $(document).ready(function(){
    $('.reviews__slider').slick({

        dots: false, 
        arrows: true,
        centerMode: true,
        slidesToShow: 1,
    });
 });

 $(document).ready(function(){
    $('#slider-6').slick({

        dots: false, 
        arrows: false,
        centerMode: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        asNavFor: '.menu__slider__big, .menu__slider__small',
        draggble: false,
        swipe: false,
    });

 });

