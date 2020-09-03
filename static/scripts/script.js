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
        if ($(this).hasClass('active')){
            $(this).removeClass('active')
            $(this).children('.answer').slideUp()
        }else{
            $(this).addClass('active');  
            $(this).children('.answer').slideDown()
            $(this).siblings().removeClass('active')
            $(this).siblings().children('.answer').slideUp()

        }
    });

    


    let filter = $("[data-filter]");

    filter.on("click", function(){
       
        let cat =   $(this).data('filter');
        

        $("[data-cat]").each(function(){

            let workcat = $(this).data("cat");

            if (workcat != cat){

                $(this).addClass('hide')

            }else{
                $(this).removeClass('hide')
            }

        })

    });



    });
