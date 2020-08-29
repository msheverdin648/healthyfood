$(document).ready(function(){
    $(".programms__big__block").on('click', function(){
        $(this).siblings().removeClass("active");
        $(this).addClass('active');
    });

    $(".programms__small__items").on('click', function(){
        $(this).siblings().removeClass("active");
        $(this).addClass('active');
    });


    $(".buy-now__block__days__item").on('click', function(){
        $(this).siblings().removeClass("active");
        $(this).addClass('active');
    });

    $(".questions__section__item").on('click', function(){
        $(this).siblings().removeClass("active");
        $(this).addClass('active');
    });

    $(".questions__answers__item").on('click', function(){
        $(this).siblings().removeClass("active");
        $(this).addClass('active');  

        $(this).children('.answer').siblings().removeClass("active");
        $(this).children('.answer').addClass('active'); 

        if ($(this).hasClass('active') && $(this).children('.answer').hasClass('active')){
            $(this).children('.answer').show()
        }else{
            $(this).children('.answer').hide()
        }
    });
    });
