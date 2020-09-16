from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy

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
    Cart)




class Base(View):
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
        'categories' :categories
        })

class MenuView(View):
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
        })




class MenuFilter(ListView):


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
            'cat' : cat, 
        })



class CategoryDetailView(DetailView):
    model = MenuCategory
    queryset = MenuCategory.objects.all()
    context_objects_name = 'category'
    template_name = 'main_page/menu.html'
    slug_url_kwarg = 'slug'

class Account(View):

    form_class = UserCreationForm


    def get(self, request):
        return render(request, 'main_page/personal-account.html', {
            
        })
    




