from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = ['*']
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "bgg-cache",
        "TIMEOUT": 2592000,
    }
}