from django.urls import path
from . import views


urlpatterns = [
    path('', views.Base.as_view(), name = 'headers'),
    path('personal-account/', views.Account.as_view(), name='account'),
    path('filter/', views.MenuFilter.as_view(), name = 'filter'),
    path('menu/<str:menu_cat>/', views.MenuView.as_view(), name = 'menu'),    
    path('add-to-cart/<str:food_name>', views.AddToCartView.as_view(), name = 'add-to-cart'),
    path('delete-from-cart/<str:food_name>', views.DeleteFromCartView.as_view(), name = 'delete-from-cart'),
    path('change-count/<str:food_name>', views.ChangeCountView.as_view(), name = 'change_count')
]




