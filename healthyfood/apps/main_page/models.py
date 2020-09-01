from django.db import models
from colorfield.fields import ColorField




class HeaderSlider(models.Model):

    slider_header= models.CharField(("Обозначение о чем этот слайд"), max_length=50, null = True, blank = True)
    main_text = models.CharField(("Главный текст слайдера"), max_length=300)
    small_text = models.CharField(("Маленький текст слайдера"), max_length=200, null = True, blank = True)
    button = models.CharField( ("Текст кнопки"), max_length=50, null = True, blank = True)

    def __str__(self):
        return self.slider_header

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Слайд хедера'
        verbose_name_plural = 'Слайды хедера'



class PageSlider(models.Model):

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Слайд анонса'
        verbose_name_plural = 'Слайды анонса'


    
    anons_slider_text = models.CharField(("Текст слайда"), max_length=50)
    anons_slider_image = models.ImageField(("Картинка слайда"), upload_to=None, height_field=None, width_field=None, max_length=100)
    anons_slider_bgcolor = ColorField (("Цвет фона слайда"), default= '#F0F0F0' )

    

class PageHeaders(models.Model):


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Заголовоки страницы'
        verbose_name_plural = 'Заголовки страницы'

    anons_header = models.CharField(("Заголовок анонса"), max_length=100)
    anons_header_bold = models.CharField(("Выделенный текст заголовка анонса"), max_length=50, null = True, blank = True)
    calculator_header = models.CharField(("Заголовок калькулятора"), max_length=100)
    menu_header = models.CharField(("Заголовок меню"), max_length=100)
    menu_smalltext = models.CharField(("маленький текст в меню"), max_length=200)
    buy_header = models.CharField(("Заголовок 'Закажи сейчас' "), max_length=100)
    reviews_header = models.CharField(("Заголовок отзывов"), max_length=100)
    questions_header = models.CharField(("Заголовок вопросов"), max_length=100)