from .base import *
import os

DEBUG = True
ALLOWED_HOSTS = ['*']
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ['REDIS_PATH'],
        "TIMEOUT": 2592000,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": os.environ['REDIS_PASSWORD'],

        }
    }
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': os.path.join(BASE_DIR, 'frontend/bundles'),
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend/webpack-stats.json'),
    }
}