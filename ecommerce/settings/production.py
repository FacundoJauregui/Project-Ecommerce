from .base import *
import dj_database_url

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
DEBUG = True

INSTALLED_APPS += ('gunicorn',)

ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'ecommerce.wsgi.production.application'

DATABASES = {}
DATABASES['default'] = dj_database_url.parse('mysql://root2:1413@192.168.100.9:3306/django_ecommerce')

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]