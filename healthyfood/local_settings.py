import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))


SECRET_KEY = '$%6j(+%n^_c7oc0&&uuygzj^py0l)el(m3e!hni^ovfu1n=5i%'

DEBUG = True

ALLOWED_HOSTS = ['.pythonanywhere.com', '127.0.0.1']




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFIELS_DIRS = (
    [STATIC_DIR],
     )
STATIC_ROOT =  os.path.join(BASE_DIR, 'static')