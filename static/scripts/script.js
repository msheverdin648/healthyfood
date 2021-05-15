


$(document).ready(function(){

    

    function showKkal(element){
        let category = $(element).data('slug')
        console.log(category)
        $("[data-slugs]").each(function(){

            let slugs = $(this).data('slugs')

            if (category != slugs){
                
                $(this).addClass('hide')

            }else{
                $(this).removeClass('hide')
            }
        })
    }


    //Настройки активных элементов
    $('.header__navigate__burger').on('click', function(){
        $('.header__navigate__burger, .header__navigate__menuburger').toggleClass('active');
        $('body').toggleClass('lock')
    })

    $(".buy-now__block__days__item").on('click', function(){
        $(this).siblings().removeClass("active");
        $(this).addClass('active');
    });

    $(".questions__section__item").on('click', function(){
        $(this).siblings().removeClass("active");
        $(this).addClass('active');
    });

    $(".programms__kkals__item").on('click', function(){
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

    

    $(".programms__big__block").on('click', function(){


            $(this).siblings().removeClass('active')
            $(this).addClass('active')
            
        
    })




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
            
        }else if ($(small_block2).hasClass('active') || $(small_block8).hasClass('active')){
            $(big_block1).removeClass('active');
            $(big_block3).removeClass('active');
            $(big_block4).removeClass('active');
            $(big_block2).addClass('active');

        }else if ($(small_block3).hasClass('active') || $(small_block7).hasClass('active') || $(small_block4).hasClass('active')) {
            $(big_block1).removeClass('active');
            $(big_block2).removeClass('active');
            $(big_block4).removeClass('active');
            $(big_block3).addClass('active');
        }else if ($(small_block6).hasClass('active') || $(small_block5).hasClass('active')){
            $(big_block1).removeClass('active');
            $(big_block2).removeClass('active');
            $(big_block3).removeClass('active');
            $(big_block4).addClass('active');
        }else if ($(small_block9).hasClass('active') || $(small_block10).hasClass('active')){
            $(big_block1).removeClass('active');
            $(big_block2).removeClass('active');
            $(big_block3).removeClass('active');
            $(big_block4).removeClass('active');
        }
    };





    $(".programms__small__items").on('click', function(){
        $(this).addClass('active');
        $(this).siblings().removeClass('active');
        make_small_block_active();
        showKkal(this);
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
        else if (activity == 1){
            activity_num = +1.4;
        }
        if(gender == 0){
           oow  = (9.99 * weight)+(6.25 * height) - (4.92 * age) + 5; 
        }else if (gender == 1){
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
            if (kkal <= 1000){
                form_out.value = 'healthy800'
            }else if(kkal >=1000 && kkal <= 1200){
                form_out.value = 'healthy1000'
            }else if(kkal >=1200 && kkal <= 1400){
                form_out.value = 'healthy1200'
            }else if(kkal > 1400){
                form_out.value = 'healthy1400'
            }
        }else if (need_weight == 1){
            if (kkal <= 1200){
                form_out.value = 'sports1000'
            }else if(kkal >=1200 && kkal <= 1600){
                form_out.value = 'sports1400'
            }else if(kkal >=1600 && kkal <= 2000){
                form_out.value = 'sports1800'
            }else if(kkal > 2000){
                form_out.value = 'sports2000'
            }
        }else if (need_weight == 2){
            if (gender == 0){
                form_out.value = 'balanced1800'
            }else if(gender == 1){
                form_out.value = 'balanced1600'
            }
        }
    });


    const path=document.location.href



    if (path == small_block1.href){
        $('#small__block-1').addClass('active')
        make_small_block_active()
    }else if(path == small_block2.href){
        $('#small__block-2').addClass('active')
        make_small_block_active()
    }else if(path == small_block3.href){
        $('#small__block-3').addClass('active')
        make_small_block_active()
    }else if(path == small_block4.href){
        $('#small__block-4').addClass('active')
        make_small_block_active()
    }else if(path == small_block5.href){
        $('#small__block-5').addClass('active')
        make_small_block_active()
    }else if(path == small_block6.href){
        $('#small__block-6').addClass('active')
        make_small_block_active()
    }else if(path == small_block7.href){
        $('#small__block-7').addClass('active')
        make_small_block_active()
    }else if(path == small_block8.href){
        $('#small__block-8').addClass('active')
        make_small_block_active()
    }else if(path == small_block9.href){
        $('#small__block-9').addClass('active')
        make_small_block_active()
    }else if(path == small_block10.href){
        $('#small__block-10').addClass('active')
        make_small_block_active()
    }

});


