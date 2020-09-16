from django.db import models
from django.contrib.auth.models import User



'''
Категория меню
Блюдо
Дни недели
Меню


Заказанные блюда
Заказ

Покупатель

'''




class MenuCategory(models.Model):

    name = models.CharField(("Имя категории"), max_length=100)
    gramm = models.CharField(("Диапазон ккал"), max_length=20)
    slug = models.SlugField(("Ссылка категории"))


    class Meta:
        verbose_name = ("Категория меню")
        verbose_name_plural = ("Категории меню")

    def __str__(self):
        return " {}: {} ккал".format(self.name, self.gramm)

    def get_absolute_url(self):
        return reverse("menu", kwargs={"slug": self.slug})
    
    

class Customer(models.Model):

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Пользователь '
        verbose_name_plural = 'Пользователи'
    

    user = models.ForeignKey(User, verbose_name=("Пользователь"), on_delete=models.CASCADE)
    phone = models.CharField(("Номер телефона"), max_length=20)
    adress = models.CharField(("Адрес"), max_length=255)

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)
    

class HeaderSlider(models.Model):

    slider_header= models.CharField(("Обозначение о чем этот слайд"), max_length=50, null = True, blank = True)
    main_text = models.CharField(("Главный текст слайдера"), max_length=300)
    small_text = models.CharField(("Маленький текст слайдера"), max_length=200, null = True, blank = True)
    button = models.CharField( ("Текст кнопки"), max_length=50, null = True, blank = True)

    def __str__(self):
        return self.main_text

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


    anons_slider_name = models.CharField(("Имя слайда"), max_length=50)
    anons_slider_text = models.CharField(("Текст слайда"), max_length=50)
    anons_slider_image = models.ImageField(("Картинка слайда"), upload_to='img', height_field=None, width_field=None, max_length=100)
    anons_slider_bgcolor = models.CharField (("Цвет фона слайда"), default= '#F0F0F0',  max_length=7)
    anons_slider_link = models.CharField(("Сылка слайда"), max_length=200)

    def __str__(self):
        return self.anons_slider_name   

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

class ProgrammsBig(models.Model):

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Большой блок '
        verbose_name_plural = 'Большие блоки'

    big_text = models.CharField(("Название блока"), max_length=50)
    big_img = models.FileField(("Картинка блока"), upload_to='img')

    def __str__(self):
        return self.big_text

class ProgrammsSmall(models.Model):

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Маленький блок '
        verbose_name_plural = 'Маленькие блоки'

    name = models.CharField(("Название маленького блока"), max_length=50)
    small_img = models.FileField(("Картинка блока"), upload_to='img')
    cat = models.IntegerField(("Номер блока"), max_length=2)
    category = models.ForeignKey(MenuCategory, verbose_name=("Категория меню привязываемая к этому блоку"), on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

class Days(models.Model):

    days_name = models.CharField(('День недели'), max_length = 20 )

    def __str__(self):
        return self.days_name 

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'  


class Food(models.Model):
    class Meta:
        verbose_name = ("Блюдо ")
        verbose_name_plural = ("Блюда")

    def __str__(self):
        return self.name

    name = models.CharField(("Название блюда"), max_length=100)
    menu_discription = models.CharField(("Описание блюда"), max_length=500)
    big_img = models.ImageField(("Картинка большого слайда"), upload_to='img', height_field=None, width_field=None, max_length=None)
    small_img = models.ImageField(("Картинка маленького слайда"), upload_to='img', height_field=None, width_field=None, max_length=None)
    kkal = models.CharField(("Колличество калорий"), max_length=20)
    gramm = models.CharField(("Колличество грамм"), max_length=20)
    price = models.CharField(("Цена блюда"), max_length=10)
    discount = models.CharField(("Цена со скидкой, если есть"), max_length=10, null=True, blank = True)
    days_list = models.ManyToManyField(Days, verbose_name = "Дни недели", related_name='days')






class Menu(models.Model):
    class Meta:
        verbose_name = ("Меню")
        verbose_name_plural = ("Меню")

    def __str__(self):
        return "Меню: {} {} ккал".format(self.category.name, self.category.gramm)


    category = models.ForeignKey(MenuCategory, verbose_name=("Категория меню"), on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(Food, verbose_name= ("Позиции меню"))

    def get_slug(self):
        return category.slug

class Reviews(models.Model):

    class Meta:
        verbose_name = ("Отзыв")
        verbose_name_plural = ("Отзывы")

    def __str__(self):
        return self.name


    name = models.CharField(("Имя автора"), max_length=50)
    age = models.CharField(("Возраст"), max_length=10)
    text = models.CharField(("Текст отзыва"), max_length=500)
    before_img = models.ImageField(('Фото "до"'), upload_to='img', height_field=None, width_field=None, max_length=None)
    after_img = models.ImageField(('Фото "после"'), upload_to='img', height_field=None, width_field=None, max_length=None)



class QuestionsAnswers(models.Model):


    WEIGTH = 'weight'
    PRODUCTS = 'products'
    TARIFS = 'tarifs'

    CHOICE_GROUP = {
      ( WEIGTH, 'Вес'),
        (PRODUCTS, 'Продукты'),
        (TARIFS, 'Тарифы') ,
    }




    question = models.CharField(("Вопрос"), max_length=200)
    answer = models.CharField(("Ответ"), max_length=1000)
    group = models.CharField(("Группа вопросов"), max_length=20, choices = CHOICE_GROUP, default = PRODUCTS)

    class Meta:
        verbose_name = ("Вопрос и ответ")
        verbose_name_plural = ("Вопросы и ответы")

    def __str__(self):
        return self.question


    
class Order(models.Model):

    customer = models.ForeignKey(Customer, verbose_name=("Заказчик"), on_delete=models.CASCADE)
    product = models.ForeignKey(Food, verbose_name=("Имя продукта"), on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(("Общая цена"), max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = ("Заказ")
        verbose_name_plural = ("Заказы")

    def __str__(self):
        return 'Продукт для общего заказа {}'.format(self.product.name)


class Cart(models.Model):

    owner = models.ForeignKey(Customer, verbose_name=("Заказчик"), on_delete=models.CASCADE)
    products = models.ManyToManyField(Order , verbose_name=("Заказанные блюда"))
    total_products = models.PositiveIntegerField(("Кол-личество продукта"), default=0)
    final_price = models.DecimalField(("Общая цена заказа"), max_digits=5, decimal_places=2)
    

    class Meta:
        verbose_name = ("Корзина")
        verbose_name_plural = ("Корзины покупателей")

    def __str__(self):
        return str(self.id)





