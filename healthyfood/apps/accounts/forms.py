from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
  email = forms.EmailField(max_length=254, help_text='Это поле обязательно')
  name = forms.CharField(max_length=255, help_text="Это поле обязательно")
  sename = forms.CharField(max_length=255, help_text="Это поле обязательно")

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2', 'name', 'sename')