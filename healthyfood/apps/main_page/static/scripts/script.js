$(document).ready(function(){


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

        

        


    $(".programms__small__items").on('click', function(){
        $(this).addClass('active');
        make_small_block_active();
    });

    
    function make_small_block_active(){
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
    };





    $(".programms__small__items").on('click', function(){
        $(this).addClass('active');
        $(this).siblings().removeClass('active');
        make_small_block_active();
    });

    aceept_button.on('click', function(){
        let gender = document.getElementById("gender").options.selectedIndex;
        let activity = document.getElementById("activity").options.selectedIndex;
        let height = parseInt(document.getElementById("height").value);
        let age = parseInt(document.getElementById("age").value);
        let weight = parseInt(document.getElementById("weight").value);
        let need_weight = document.getElementById("need_weight").options.selectedIndex
        let form_out = document.getElementById("form_out")

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



        if (need_weight == 0){
            $('#small__block-1').addClass('active');
            $('#small__block-1').siblings().removeClass('active')
            make_small_block_active();
        }else if (need_weight == 1){
            $('#small__block-2').addClass('active');
            $('#small__block-2').siblings().removeClass('active')
            make_small_block_active();
        }else if (need_weight == 2){
            $('#small__block-3').addClass('active');
            $('#small__block-3').siblings().removeClass('active')
            $(big_block2).addClass('active')
            $(big_block2).siblings().removeClass('active')
        }



        //Ссылки калькулятора
        if (need_weight == 0){
            if (kkal >=800 && kkal <= 1000){
                form_out.value = 'HEALTHY800'
            }else if(kkal >=1000 && kkal <= 1200){
                form_out.value = 'HEALTHY1000'
            }else if(kkal >=1200 && kkal <= 1400){
                form_out.value = 'HEALTHY1200'
            }else if(kkal >=1400 && kkal <= 1600){
                form_out.value = 'HEALTHY1400'
            }
        }else if (need_weight == 1){
            if (kkal >=1400 && kkal <= 1600){
                form_out.value = 'PERFECTFITLIGHT'
            }else if(kkal >=1600 && kkal <= 1800){
                form_out.value = 'PERFECTFITMEDIUM'
            }else if(kkal >=2000 && kkal <= 3000){
                form_out.value = 'PERFECTFITSTRONGMEN'
            }
        }else if (need_weight == 2){
            if (gender == 0){
                form_out.value = 'BALANCEDMAN'
            }else if(gender == 1){
                form_out.value = 'BALANCEDWOMAN'
            }
        }


    });



});


