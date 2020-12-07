from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect 

from .models import UserMessage
from .forms import MessageForm



class TakeMessageView(View):

    def post(self, request, *args, **kwargs):
        message_text = request.POST.get('communication')
        user_phone = request.POST.get('phone')
        author = request.POST.get('name')
        message = UserMessage.objects.create(
            author=author, message_text=message_text, phone=user_phone
        )
        message.save()
        return HttpResponseRedirect('/')

