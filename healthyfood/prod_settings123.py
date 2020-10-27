import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



SECRET_KEY = '$1283u@*$2d1+%n^_c7o321@!$51_"&uuygzj^pyawdlo120e-12g-)_e!hni^ovfu1n=5i%'


DEBUG = False

ALLOWED_HOSTS = ['http://healthyfood.uz','127.0.0.1', '49.12.75.213', 'www.healthyfood.uz', 'healthyfood.uz']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'healthy_db',
        'USER': 'admindb',
        'PASSWORD':'gh&^brtVJ%^vhr^gu5F', 
        'HOST': 'localhost',
        'PORT': '5432'
    }
}





#STATIC_DIR = os.path.join(BASE_DIR, 'static')
#STATICFIELS_DIRS = (
   # os.path.join(PROJECT_ROOT, 'static'),
    # )

STATIC_ROOT =  os.path.join(BASE_DIR, 'static')
