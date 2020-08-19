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