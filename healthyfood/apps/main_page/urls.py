from django.urls import path
from . import views


urlpatterns = [
    path('', views.Base.as_view(), name = 'headers'),
    path('personal-account/', views.Account.as_view(), name='account'),
    path('filter/', views.MenuFilter.as_view(), name = 'filter'),
    path('menu/<menu_cat>/', views.MenuView.as_view(), name = 'menu')
      
    
]




