from django.urls import path
from . import views


urlpatterns = [
    path('make_message/', views.TakeMessageView.as_view(), name = 'make_message'),
]
