from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from main_page.models import HeaderSlider, PageSlider, PageHeaders, ProgrammsBig, ProgrammsSmall, MenuSlider, Reviews, QuestionsAnswers, Days, MenuList



class MenuCat:
    
    def get_cat(self):
        cat_list = MenuList.objects.all()
        lose_weight = cat_list.get(name='HEALTHY800').name
        for_sportsmen = cat_list.get(name='PERFECTFITLIGHT').name
        balanced_eat = cat_list.get(name='BALANCEDMAN').name
        individual_eat = cat_list.get(name='INDIVIDUAL').name
        breast_eat = cat_list.get(name='BREASTEAT').name
        ill_eat = cat_list.get(name='ILLFOOD').name
        vegan_eat = cat_list.get(name='VGETERIAN').name
        protein_eat = cat_list.get(name='PROTEIN').name
        office_pack = cat_list.get(name='OFFICEPACK').name
        vip_menu = cat_list.get(name='VIP').name
        programms =[
                {'index': '1',  'name': lose_weight},
                {'index': '2',  'name': for_sportsmen},
                {'index': '3',  'name': balanced_eat},
                {'index': '4',  'name': individual_eat},
                {'index': '5',  'name': breast_eat},
                {'index': '6',  'name': ill_eat},
                {'index': '7',  'name': vegan_eat},
                {'index': '8',  'name': protein_eat},
                {'index': '9',  'name': office_pack},
                {'index': '10',  'name': vip_menu},
               ]
        return programms


class Base(View, MenuCat):
    def get(self, request):
        menu = MenuSlider.objects.all()
        headers = PageHeaders.objects.all()
        header_slider = HeaderSlider.objects.all()
        page_slider = PageSlider.objects.all()
        programms_big = ProgrammsBig.objects.all()
        programms_small = ProgrammsSmall.objects.all()
        reviews = Reviews.objects.all()
        reviews_count = reviews.count()
        questions = QuestionsAnswers.objects.all()
        days  = Days.objects.all()
        cat = self.get_cat()
        return render(request, 'main_page/page.html', {"headers": headers,
        'header_slider': header_slider,
        'page_slider': page_slider,
        'programms_big': programms_big,
        'programms_small': programms_small,
        'reviews': reviews,
        "reviews_count" : reviews_count,
        'questions': questions,
        'menu': menu,
        'days': days,
        'cat' : cat,
        })

class MenuView(MenuCat, View):
    model = MenuList
    template_name = "main_page/menu.html"
    
    def get(self, request,menu_cat):
        headers = PageHeaders.objects.all()
        header_slider = HeaderSlider.objects.all()
        page_slider = PageSlider.objects.all()
        programms_big = ProgrammsBig.objects.all()
        programms_small = ProgrammsSmall.objects.all()
        reviews = Reviews.objects.all()
        reviews_count = reviews.count()
        questions = QuestionsAnswers.objects.all()
        days  = Days.objects.all()
        cat = self.get_cat()
        menu_list = MenuList.objects.filter(name = menu_cat)
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
            'menu_list': menu_list,
        })




class MenuFilter(ListView, MenuCat):


    model = MenuList
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
        cat = self.get_cat()
        menu_list = MenuList.objects.filter(name__in = self.request.GET.getlist('menu_cat'))
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
            'menu_list': menu_list,
        })





class Account(MenuCat, View):

    form_class = UserCreationForm


    def get(self, request):
        return render(request, 'main_page/personal-account.html', {
            
        })
    




