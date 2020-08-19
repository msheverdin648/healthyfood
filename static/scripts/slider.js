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
        slidesToShow: 5,
        arrows: true,
        vertical: true,
        slidesToScroll: 1,

    });
 });


 $(document).ready(function(){
    $('.menu__slider__big').slick({

        dots: false, 
        arrows: true,

    });
 });