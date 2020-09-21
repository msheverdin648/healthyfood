from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class PostImages(models.Model):
    image_name = models.CharField(("Название картинки"), max_length=255)
    post_img = models.ImageField(("Картинки блога"), upload_to='blog_images')
    post = models.ForeignKey("blog.Post", verbose_name=("Пост в который нужно добавить эту картинку"), on_delete=models.CASCADE, related_name='related_post', blank=True, null=True)

    class Meta:
        verbose_name = ("Картинка поста")
        verbose_name_plural = ("Картинки поста")

    def __str__(self):
        return "{} для {}".format(self.image_name, self.post)



class Post(models.Model):

    
    author = models.CharField(("Имя автора(необязательно)"), max_length=255, blank=True, null=True)
    post_name = models.CharField(("Заголовок поста"), max_length=255)
    post_text = models.TextField(("Содержимое поста"), blank=True, null=True)
    images = models.ManyToManyField("blog.PostImages", verbose_name=("Картинки блога"), related_name='related_postimages', blank=True, null=True)
    date = models.DateField(("Дата публикации"), auto_now=True)

    class Meta:
        verbose_name = ("Пост")
        verbose_name_plural = ("Пост")

    def __str__(self):
        return self.post_name



class PostComments(models.Model):

    author = models.ForeignKey(User, verbose_name=("Имя автора"), on_delete=models.CASCADE)
    comment_text = models.TextField(("Текст комментария"))
    create_date = models.DateField(("Дата комментирования"), auto_now=True)
    post = models.ForeignKey(Post, verbose_name=("Комментируемый пост"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Комментарий поста")
        verbose_name_plural = ("Комментарии поста")

    def __str__(self):
        return "{} ({}) ".format(self.author, self.post )