from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'ecommerce.wsgi.local.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_ecommerce',
        'HOST': '192.168.100.9',
        'USER': 'root2',
        'PASSWORD': '1413',
        'PORT': '3306',
    }
}

AUTH_PASSWORD_VALIDATORS = [

]