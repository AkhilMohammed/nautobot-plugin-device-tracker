
import os
import re

from nautobot.core.settings import *
#from nautobot.core.settings_func import is_truthy, parse_redis_connection




SECRET_KEY = "9.V$@Kxkc@@Kd@z<a/=.J-Y;rYc79<y@](9o9(L(*sS)Q+ud5P"


DEBUG = True  # Set True for local dev only
ALLOWED_HOSTS = ["*"]  # Adjust for your environment


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nautobot',
        'USER': 'nautobot',
        'PASSWORD': 'nautobot',
        'HOST': 'db',
        'PORT': 5432,
    }
}

PLUGINS = []
AUTH_USER_MODEL = "users.User"

PLUGINS_CONFIG={}
#PLUGINS_CONFIG = {
#    'nautobot_plugin_example': {
#        'example_setting': True,
#    },
#}


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
