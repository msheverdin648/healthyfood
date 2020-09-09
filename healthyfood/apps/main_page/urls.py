from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.Base.as_view(), name = 'headers'),
    path('menu/<menu_cat>/', views.MenuView.as_view(), name = 'menu')
    
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)