from .base import *
import os

DEBUG = True
ALLOWED_HOSTS = ['*']
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ['REDIS_PATH'],
        "TIMEOUT": 1000, # 2592000,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": os.environ['REDIS_PASSWORD'],

        }
    }
}