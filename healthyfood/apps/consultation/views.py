from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect 

from .models import UserMessage
from .forms import MessageForm



class TakeMessageView(View):

    def post(self, request, *args, **kwargs):
        message_text = request.POST.get('communication')
        message = UserMessage.objects.create(
            author=request.user, message_text=message_text
        )
        message.save()
        return HttpResponseRedirect('/')

