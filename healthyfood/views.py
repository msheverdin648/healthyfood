from django.db import transaction
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect 


from .mixins import CartMixin
from .forms import OrderForm
from main_page.models import (
    HeaderSlider, 
    PageSlider, 
    PageHeaders, 
    ProgrammsBig, 
    ProgrammsSmall, 
    Reviews, 
    QuestionsAnswers, 
    Days,
    MenuCategory,
    Menu,
    Customer, 
    Food,
    Cart,
    Order,
    Buy
    )




class AddToCartView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        food_name = kwargs.get('food_name')
        food = Food.objects.get(name=food_name)
        order, created = Order.objects.get_or_create(
            customer=self.cart.owner, cart = self.cart, product=food
        )
        if created:
            self.cart.products.add(order)
        self.cart.cart_save()
        return HttpResponseRedirect('/personal-account/')


class DeleteFromCartView(View):

    def get(self, request, *args, **kwargs):

        food_name = kwargs.get('food_name')
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objects.get(owner=customer, in_order=False)
        food = Food.objects.get(name=food_name)
        order = Order.objects.get(
            customer=cart.owner, cart=cart, product=food
        )
        cart.products.remove(order)
        order.delete()
        return HttpResponseRedirect('/personal-account/')



class ChangeCountView(View):

    def post(self, request, *args, **kwargs): 
        food_name = kwargs.get('food_name')
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objects.get(owner=customer, in_order=False)
        food = Food.objects.get(name=food_name)
        order = Order.objects.get(
            customer=cart.owner, cart=cart, product=food
        )
        count = int(request.POST.get('count'))
        order.count = int(count)
        order.save()
        cart.cart_save()
        return HttpResponseRedirect('/personal-account/') 



class Base(CartMixin, View):
    def get(self, request):
        headers = PageHeaders.objects.all()
        header_slider = HeaderSlider.objects.all()
        page_slider = PageSlider.objects.all()
        programms_big = ProgrammsBig.objects.all()
        programms_small = ProgrammsSmall.objects.all()
        reviews = Reviews.objects.all()
        reviews_count = reviews.count()
        questions = QuestionsAnswers.objects.all()
        days  = Days.objects.all()
        categories = MenuCategory.objects.all()
        menu = Menu.objects.all()
        short_slugs = categories.distinct().values('short_slug', 'full_slug', 'gramm')
        slugs = short_slugs.values('short_slug')
        healthy = short_slugs.filter(short_slug='healthy')

        print(slugs)

        return render(request, 'main_page/page.html',{
        "headers": headers,
        'header_slider': header_slider,
        'page_slider': page_slider,
        'programms_big': programms_big,
        'programms_small': programms_small,
        'reviews': reviews,
        "reviews_count" : reviews_count,
        'questions': questions,
        'days': days,
        'categories' :categories,
        'cart': self.cart,
        'menu': menu,
        'short_slugs':short_slugs,
        'healthy': healthy,
        'slugs':slugs,


        })

class MenuView(CartMixin, View):
    def get(self, request, menu_cat):
        headers = PageHeaders.objects.all()
        header_slider = HeaderSlider.objects.all()
        page_slider = PageSlider.objects.all()
        programms_big = ProgrammsBig.objects.all()
        programms_small = ProgrammsSmall.objects.all()
        questions = QuestionsAnswers.objects.all()
        days  = Days.objects.all()
        request_category = MenuCategory.objects.get(full_slug = menu_cat)
        reviews = Reviews.objects.filter(category = request_category)
        reviews_count = reviews.count()
        categories = MenuCategory.objects.all()
        for a in range(reviews_count):
            reviews[a].save_num(a)
        menu = Menu.objects.filter(category = request_category)
        short_slugs = categories.distinct().values('short_slug', 'full_slug', 'gramm')
        slugs = short_slugs.values('short_slug')
        healthy = short_slugs.filter(short_slug='healthy')
        return render(request, 'main_page/menu.html', {
            "headers": headers,
            'header_slider': header_slider,
            'page_slider': page_slider,
            'programms_big': programms_big,
            'programms_small': programms_small,
            'reviews': reviews,
            "reviews_count" : reviews_count,
            'questions': questions,
            'days': days,
            'menu': menu,
            'cart': self.cart,
            'short_slugs': short_slugs,
            'slugs': slugs,
            'healthy': healthy,            
        })




class MenuFilter(CartMixin, ListView):


    template_name = "main_page/menu.html"
    
    def get(self, request):
        headers = PageHeaders.objects.all()
        header_slider = HeaderSlider.objects.all()
        page_slider = PageSlider.objects.all()
        programms_big = ProgrammsBig.objects.all()
        programms_small = ProgrammsSmall.objects.all()
        reviews = Reviews.objects.all()
        reviews_count = reviews.count()
        questions = QuestionsAnswers.objects.all()
        days  = Days.objects.all()
        request_category = MenuCategory.objects.get(slug = request.GET.get('menu_cat'))
        menu = Menu.objects.filter(category = request_category)
        return render(request, 'main_page/menu.html', {
            "headers": headers,
            'header_slider': header_slider,
            'page_slider': page_slider,
            'programms_big': programms_big,
            'programms_small': programms_small,
            'reviews': reviews,
            "reviews_count" : reviews_count,
            'questions': questions,
            'days': days,
            'menu' : menu, 
            'cart': self.cart
        })



class CategoryDetailView(DetailView):
    model = MenuCategory
    queryset = MenuCategory.objects.all()
    context_objects_name = 'category'
    template_name = 'main_page/menu.html'
    slug_url_kwarg = 'slug'

class Account(CartMixin, View):

    def get(self, request, *args, **kwargs):

        customer = Customer.objects.filter(user = request.user)
        return render(request, 'main_page/personal-account.html', {
            'customer': customer,
            'cart' : self.cart,

        })
    

class CheckOutView(CartMixin, View):

    def get(self, request, *args, **kwargs):


        form = OrderForm(request.POST or None)
        customer = Customer.objects.filter(user = request.user)
        return render(request, 'main_page/checkout.html', {
            'customer': customer,
            'cart' : self.cart,
            'form': form
        })
    

class MakeOrderView(CartMixin, View):
    

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        customer = Customer.objects.get(user=request.user)
        user = User.objects.get(username=request.user.username)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = customer
            new_order.first_name = form.cleaned_data['first_name']
            new_order.last_name = form.cleaned_data['last_name']
            new_order.phone = form.cleaned_data['phone']
            new_order.address = form.cleaned_data['address']
            new_order.buying_type = form.cleaned_data['buying_type']
            new_order.comment = form.cleaned_data['comment']
            new_order.save()
            self.cart.in_order = True
            self.cart.save()
            new_order.cart = self.cart
            new_order.save()
            customer.orders.add(new_order)
            customer.phone = new_order.phone
            customer.adress = new_order.address
            customer.save()
            user.first_name = new_order.first_name
            user.last_name = new_order.last_name
            user.save()
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('checkout')


class MyOrdersView(CartMixin, View):

    def get(self, request, *args, **kwargs):

        customer = Customer.objects.get(user = request.user)
        orders_list = Buy.objects.filter(customer=customer)
        context = {
            'customer': customer,
            'orders_list':orders_list
        }
        return render(request, 'main_page/orders.html', context)


