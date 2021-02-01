from modeltranslation.translator import register, TranslationOptions
from .models import (
    PageHeaders, 
    HeaderSlider,
    Food, 
    MenuCategory, 
    ProgrammsBig, 
    ProgrammsSmall, 
    QuestionsAnswers, 
    Reviews, 
    PageSlider,
    Days
    )

@register(PageHeaders)
class PageHeadersTranslationOptions(TranslationOptions):
    fields = (
        'anons_header',
        'anons_header_bold',
        'calculator_header',
        'menu_header',
        'menu_smalltext',
        'buy_header',
        'reviews_header',
        'questions_header',
    )


@register(MenuCategory)
class MenuCategoryTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(HeaderSlider)
class HeaderSliderTranslationOptions(TranslationOptions):
    fields = (
        'slider_header',
        'main_text',
        'small_text',
        'button',
    )



@register(PageSlider)
class PageSliderTranslationOptions(TranslationOptions):
    fields = (
        'anons_slider_name',
        'anons_slider_text',
    )

@register(ProgrammsBig)
class ProgrammsBigTranslationOptions(TranslationOptions):
    fields = (
        'big_text',
    )


@register(ProgrammsSmall)
class ProgrammsSmallTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )

    
@register(Days)
class DaysTranslationOptions(TranslationOptions):
    fields = (
        'days_name',
    )


@register(Food)
class FoodTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'menu_discription',
    )

@register(Reviews)
class ReviewsTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'age',
        'text',
    )
@register(QuestionsAnswers)
class QuestionsAnswersTranslationOptions(TranslationOptions):
    fields = (
        'question',
        'answer',
    )
