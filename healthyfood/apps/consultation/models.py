from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserMessage(models.Model):


    author = models.CharField(("Имя автора"), max_length=50)
    message_text = models.TextField(("Текст сообщения"))
    sending_date = models.DateTimeField(("Дата отправки данного сообщения"), auto_now=True)
    phone = models.CharField(("Телефон автора"), max_length=20)


    class Meta:
        verbose_name = ("Сообщение от пользователя")
        verbose_name_plural = ("Сообщения от пользователей")

    def __str__(self):
        return "Сообщение от пользователя '{} {} ' {}".format(self.author, self.phone, self.message_text)


