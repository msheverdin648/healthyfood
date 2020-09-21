from django.contrib import admin

from .models import Post, PostComments, PostImages


admin.site.register(Post)
admin.site.register(PostComments)
admin.site.register(PostImages)
