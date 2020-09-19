from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect 


from .mixins import CartMixin

from .models import (
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
    Order)




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
        'cart': self.cart
        })

class MenuView(CartMixin, View):
    template_name = "main_page/menu.html"
    queryset = Menu.objects.all()
    def get(self, request, menu_cat):
        headers = PageHeaders.objects.all()
        header_slider = HeaderSlider.objects.all()
        page_slider = PageSlider.objects.all()
        programms_big = ProgrammsBig.objects.all()
        programms_small = ProgrammsSmall.objects.all()
        reviews = Reviews.objects.all()
        reviews_count = reviews.count()
        questions = QuestionsAnswers.objects.all()
        days  = Days.objects.all()
        request_category = MenuCategory.objects.get(slug = menu_cat)
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
            'menu': menu,
            'cart': self.cart,
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
    




