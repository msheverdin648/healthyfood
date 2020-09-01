from django.http import HttpResponse
from django.shortcuts import render
from .models import HeaderSlider, PageSlider, PageHeaders, ProgrammsBig, ProgrammsSmall


def index(request):

    header_slides = HeaderSlider.objects.all()
    page_slides = PageSlider.objects.all()
    page_headers = PageHeaders.objects.get(id=1)
    big_block = ProgrammsBig.objects.all()
    small_block = ProgrammsSmall.objects.all()
    return render(request, 'main_page/page.html', {'header_slides': header_slides,
    'headers': page_headers,
    'page_slides': page_slides,
    'big_block': big_block,
    'small_block': small_block,

     

    
    })