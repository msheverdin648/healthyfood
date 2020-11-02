from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class MenuCategory(models.Model):

    name = models.CharField(("Имя категории"), max_length=100)
    gramm = models.CharField(("Диапазон ккал"), max_length=20)
    full_slug = models.SlugField(("Ссылка на меню"), null=True, blank=True)   
    short_slug = models.SlugField(("Ссылка на категорию"), null=True, blank=True)


    class Meta:
        verbose_name = ("Категория меню")
        verbose_name_plural = ("Категории меню")

    def __str__(self):
        return " {}: {} ккал".format(self.name, self.gramm)
    

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
    anons_slider_link = models.CharField(("Сылка слайда"), max_length=200, default="#")

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
    cat = models.IntegerField(("Номер блока"))
    slug = models.SlugField(("Короткая ссылка категории меню"))

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
    protein = models.CharField(("Колличество белков"), max_length=20, default='0')
    fats = models.CharField(("Колличество жиров"), max_length=20, default='0')
    carbohydrates = models.CharField(("Колличество углеводов"), max_length=20, default='0')
    price = models.DecimalField(("Цена блюда"), max_digits=9, decimal_places=2)
    discount = models.DecimalField(("Цена со скидкой, если есть"),  max_digits=9, decimal_places=2, null=True, blank = True)
    days_list = models.ManyToManyField(Days, verbose_name = "Дни недели", related_name='days')




class Menu(models.Model):
    class Meta:
        verbose_name = ("Меню")
        verbose_name_plural = ("Меню")

    def __str__(self):
        return "Меню: {} {} ккал".format(self.category.name, self.category.gramm)


    category = models.ForeignKey(MenuCategory, verbose_name=("Категория меню"), on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(Food, verbose_name= ("Позиции меню"))
    #kkal = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)

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
    text = models.TextField(("Текст отзыва"))
    before_img = models.ImageField(('Фото "до"'), upload_to='img', height_field=None, width_field=None, max_length=None)
    after_img = models.ImageField(('Фото "после"'), upload_to='img', height_field=None, width_field=None, max_length=None)
    category = models.ForeignKey(MenuCategory, verbose_name=("Меню(к которому сделан отзыв)"), on_delete=models.CASCADE)
    num = models.PositiveIntegerField(("Номер отзыва"), default=1)

    def save_num(self, rev_num, *args, **kwargs):
        self.num = rev_num+1
        super().save(*args, **kwargs)

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


    








#Настройки личного кабинета

class Customer(models.Model):

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Покупатель '
        verbose_name_plural = 'Покупатели'
    

    user = models.ForeignKey(User, verbose_name=("Имя покупателя"), on_delete=models.CASCADE)
    phone = models.CharField(("Номер телефона"), max_length=20, null=True, blank=True)
    adress = models.CharField(("Адрес"), max_length=255, null=True, blank=True)
    orders = models.ManyToManyField('Buy', verbose_name=("Заказы покупателя"), related_name='related_customer')


    def __str__(self):
        return "Покупатель: {}".format(self.user)
    



class Buy(models.Model):


    class Meta:
        verbose_name = ("Заказ")
        verbose_name_plural = ("Заказы")

    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'ready'
    STATUS_COMPLETED = 'completed'


    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Самовывоз'),
        (BUYING_TYPE_DELIVERY, 'Доставка')
    )

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ выполнен'),
    )

    customer = models.ForeignKey(Customer, verbose_name=("Заказчик"), related_name='related_orders', on_delete=models.CASCADE)
    first_name = models.CharField(("Имя"), max_length=255)
    last_name = models.CharField(("Фамилия"), max_length=255)
    phone = models.CharField(("Номер телефона"), max_length=20)
    address = models.CharField(("Адрес"), max_length=1024)
    status = models.CharField(("Статус заказа"), max_length=100, choices=STATUS_CHOICES, default=STATUS_NEW)
    buying_type = models.CharField(("Тип заказа"), max_length=100, choices=BUYING_TYPE_CHOICES, default=BUYING_TYPE_SELF)
    comment = models.TextField(("Комментарий к заказу"), blank=True, null=True)
    created_at = models.DateTimeField(("Дата создания заказа"), auto_now=True)
    cart = models.ForeignKey("main_page.Cart", verbose_name=("Корзина пользователя"), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Заказ №{}, дата заказа: {}, статус заказа: {}".format(self.id, self.created_at, self.status)


class Order(models.Model):

    customer = models.ForeignKey(Customer, verbose_name=("Заказчик"), on_delete=models.CASCADE)
    product = models.ForeignKey(Food, verbose_name=("Имя продукта"), on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(("Итоговая цена товара"), max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = ("Товар в корзине")
        verbose_name_plural = ("Товары в корзине")

    def __str__(self):
        return 'Заказанный продукт ({}) {}'.format(self.customer ,self.product.name)

    def save(self, *args, **kwargs):
        if self.product.discount:
            self.final_price = self.count * self.product.discount
        else:
            self.final_price = self.count * self.product.price
        super().save(*args, **kwargs)


class Cart(models.Model):

    owner = models.ForeignKey(Customer, verbose_name=("Заказчик"), on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Order , verbose_name=("Заказанные блюда"), blank = True)
    total_products = models.PositiveIntegerField(("Колличество блюд"), default=0)
    final_price = models.DecimalField(("Общая цена заказа"), max_digits=9, decimal_places=2, default=0)
    in_order = models.BooleanField(default = False)
    for_anonymous_user = models.BooleanField(default = False)
    class Meta:
        verbose_name = ("Корзина")
        verbose_name_plural = ("Корзины покупателей")

    def __str__(self):
        return "Корзина пользователя: {}".format(self.owner)

    def cart_save(self, *args, **kwargs):
        cart_data = self.products.aggregate(models.Sum('final_price'), models.Sum('count'))
        if cart_data.get('final_price__sum'):
            self.final_price = cart_data['final_price__sum']
        else:
            self.final_price = 0
        self.total_products = cart_data['count__sum']
        super().save(*args, **kwargs)
