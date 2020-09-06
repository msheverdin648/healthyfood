from django.http import HttpResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic.base import View
from django.views.generic import ListView 


from .models import HeaderSlider, PageSlider, PageHeaders, ProgrammsBig, ProgrammsSmall, MenuSlider, Reviews, QuestionsAnswers, MenuGroup, Days


class MenuView(View):
    def get(self, request):
        menu = MenuSlider.objects.all()
        return render(request, 'main_page/page.html', {'menu_list': menu})



def index(request):

    header_slides = HeaderSlider.objects.all()
    page_slides = PageSlider.objects.all()
    page_headers = PageHeaders.objects.get(id=1)
    big_block = ProgrammsBig.objects.all()
    small_block = ProgrammsSmall.objects.all()
    menu_slide = MenuSlider.objects.all()
    review = Reviews.objects.all()
    reviws_count = review.count()
    questions = QuestionsAnswers.objects.all()
    lose_weight = MenuSlider.objects.filter(group = 'lose_weight')
    return render(request, 'main_page/page.html', {'header_slides': header_slides,
    'headers': page_headers,
    'page_slides': page_slides,
    'big_block': big_block,
    'small_block': small_block,
    'menu': menu_slide,
    'review' : review,
    'reviws_count': reviws_count,
    'questions' : questions,
    })


class MenuGroupFilter(MenuGroup, ListView):
    def get_groups(self):
        queryset = MenuSlider.objects.filter(menu_group__in = self.request.GET.get("menu_group"))
        return queryset