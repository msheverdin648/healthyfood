from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Post, PostComments, PostImages


class BlogView(View):

    def get(self, request, *args, **kwargs):


        blog = Post.objects.all()

        context = {
            'blog': blog,
        }
        return render(request, 'blog/blog.html', context)

class PostDetail(DetailView):
    model = Post
    queryset = Post.objects.all()
    context_objects_name = 'post'
    template_name = 'blog/blog_detail.html'
