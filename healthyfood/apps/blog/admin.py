from django.contrib import admin

from .models import Post, PostComments, PostImages


admin.site.register(Post)
admin.site.register(PostImages)
