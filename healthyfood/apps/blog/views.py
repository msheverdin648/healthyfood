from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Post, PostComments, PostImages
from main_page.models import HeaderSlider


class BlogView(View):

    def get(self, request, *args, **kwargs):


        header_slider = HeaderSlider.objects.all()
        blog = Post.objects.all()
        print(header_slider)
        context = {
            'blog': blog,
            'header_slider': header_slider,
        }
        return render(request, 'blog/blog.html', context)

class PostDetail(DetailView):
    model = Post
    queryset = Post.objects.all()
    context_objects_name = 'post'
    template_name = 'blog/blog_detail.html'
