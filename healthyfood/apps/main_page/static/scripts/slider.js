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
        asNavFor: '.menu__slider__big'
    });
 });


 $(document).ready(function(){
    $('.menu__slider__big').slick({

        dots: false, 
        arrows: true,
        asNavFor: '.menu__slider__small'

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