from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic.base import View
from django.views.generic import ListView, DetailView


from .models import HeaderSlider, PageSlider, PageHeaders, ProgrammsBig, ProgrammsSmall, MenuSlider, Reviews, QuestionsAnswers, MenuGroup, Days




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
        return render(request, 'base.html', {"headers": headers,
        'header_slider': header_slider,
        'page_slider': page_slider,
        'programms_big': programms_big,
        'programms_small': programms_small,
        'reviews': reviews,
        "reviews_count" : reviews_count,
        'questions': questions
        })

class MenuView(View):
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
        return render(request, 'main_page/menu.html', {
            'menu' : menu,
            "headers": headers,
            'header_slider': header_slider,
            'page_slider': page_slider,
            'programms_big': programms_big,
            'programms_small': programms_small,
            'reviews': reviews,
            "reviews_count" : reviews_count,
            'questions': questions,
            'days' : days,
        })







class PageSlides(View):
    model = PageSlider
    queryset = PageSlider.objects.all()
    template_name = 'main_page/page.html'



class MenuGroup:
    def get_catigories(self):
        return MenuGroup.objects.all()




