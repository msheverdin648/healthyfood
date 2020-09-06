$(document).ready(function(){


    

    $(".programms__small__items").on('click', function(){
        $(this).siblings().removeClass("active");
        $(this).addClass('active');
        if ($(small_block1).hasClass('active')){

            $(big_block2).removeClass('active');
            $(big_block3).removeClass('active');
            $(big_block4).removeClass('active');
            $(big_block1).addClass('active');
            
        }else if ($(small_block2).hasClass('active')){
            $(big_block1).removeClass('active');
            $(big_block3).removeClass('active');
            $(big_block4).removeClass('active');
            $(big_block2).addClass('active');

        }else if ($(small_block3).hasClass('active') || $(small_block7).hasClass('active')) {
            $(big_block1).removeClass('active');
            $(big_block2).removeClass('active');
            $(big_block4).removeClass('active');
            $(big_block3).addClass('active');
        }else if ($(small_block6).hasClass('active') || $(small_block5).hasClass('active')){
            $(big_block1).removeClass('active');
            $(big_block2).removeClass('active');
            $(big_block3).removeClass('active');
            $(big_block4).addClass('active');
        }
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

        };
    });

    

    //Сортировка блока с вопросами и ответами по категориям
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

    //Калькулятор


    
    let aceept_button = $('.calculate__box__block__button');
    
    aceept_button.on('click', function(){
        let gender = document.getElementById("gender").options.selectedIndex;
        let activity = document.getElementById("activity").options.selectedIndex;
        let height = parseInt(document.getElementById("height").value)
        let age = parseInt(document.getElementById("age").value)
        let weight = parseInt(document.getElementById("weight").value)
        let need_weight = parseInt(document.getElementById("need_weight").value)



        console.log(height, age, weight, need_weight)
        if (activity == 0){
            activity_num = +1.2;
        }
        else{
            activity_num = +1.4;
        }
        if(gender == 0){
           oow  = (9.99 * weight)+(6.25 * height) - (4.92 * age) + 5; 
        }else{
            oow  = (9.99 * weight)+(6.25 * height) - (4.92 * age) - 161; 
        };
        kkal = oow * activity_num * 0.8;
        console.log(kkal)
    });




        let small_block1 = document.getElementById("small__block-1");
        let small_block2 = document.getElementById("small__block-2");
        let small_block3 = document.getElementById("small__block-3");
        let small_block4 = document.getElementById("small__block-4");
        let small_block5 = document.getElementById("small__block-5");
        let small_block6 = document.getElementById("small__block-6");
        let small_block7 = document.getElementById("small__block-7");
        let small_block8 = document.getElementById("small__block-8");
        let small_block9 = document.getElementById("small__block-9");
        let small_block10 = document.getElementById("small__block-10");


        let big_block1 = document.getElementById("big__block-1")
        let big_block2 = document.getElementById("big__block-2");
        let big_block3 = document.getElementById("big__block-3");
        let big_block4 = document.getElementById("big__block-4");

        

    


    });
