from .base import *
import dj_database_url

from decouple import config

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
DEBUG = False

INSTALLED_APPS += ('gunicorn',)

ALLOWED_HOSTS = ['django-ecommerce-app-fj.herokuapp.com']

WSGI_APPLICATION = 'ecommerce.wsgi.production.application'

DATABASES = {}
DATABASES['default'] = dj_database_url.config(default='mysql://root2:1413@192.168.100.9:3306/django_ecommerce')

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

#Amazon s3 Settings

AWS_ACCESS_KEY_ID = 'AKIA2XKWLYKR6YGWZQNN'

AWS_SECRET_ACCESS_KEY = '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'

AWS_STORAGE_BUCKET_NAME = 'django-ecommerce-app-fj'

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

AWS_DEFAULT_ACL = 'public-read'

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}

AWS_LOCATION= 'static'

AWS_QUERYSTRING_AUTH = False

AWS_HEADERS = {
    'Access-Control-Allow-Origin': '*',
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE= 'storage.backends.s3boto3.S3StaticStorage'

STATIC_URL= f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL= f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'