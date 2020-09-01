from django.http import HttpResponse
from django.shortcuts import render
from .models import HeaderSlider, PageSlider, PageHeaders


def index(request):

    header_slides = HeaderSlider.objects.all()
    page_slides = PageSlider.objects.all()
    return render(request, 'main_page/page.html', {'header_slides': header_slides })