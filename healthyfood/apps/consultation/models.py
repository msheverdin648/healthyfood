from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserMessage(models.Model):


    author = models.ForeignKey(User, verbose_name=("Автор сообщения"), on_delete=models.CASCADE)
    message_text = models.TextField(("Текст сообщения"))
    sending_date = models.DateTimeField(("Дата отправки данного сообщения"), auto_now=True)


    class Meta:
        verbose_name = ("Сообщение от пользователя")
        verbose_name_plural = ("Сообщения от пользователей")

    def __str__(self):
        return "Сообщение от пользователя '{} {} ' {}".format(self.author, self.author.first_name, self.sending_date)


