from .base import *
import os

DEBUG = True
ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ['REDIS_PATH'],
        "TIMEOUT": 1500,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": os.environ['REDIS_PASSWORD'],

        }
    }
}

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "frontend/bundles"),
    os.path.join(BASE_DIR, "frontend/build"),
    os.path.join(BASE_DIR, "static"),
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': os.path.join(BASE_DIR, 'frontend/build'),
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend/webpack-stats.json'),
    }
}
