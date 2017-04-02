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

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend/build"),
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = '/home/bar350/static'