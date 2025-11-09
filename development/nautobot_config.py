DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nautobot',
        'USER': 'nautobot',
        'PASSWORD': 'nautobot',
        'HOST': 'postgres',
        'PORT': 5432,
    }
}

PLUGINS = [
    'nautobot_plugin_example',
]

PLUGINS_CONFIG = {
    'nautobot_plugin_example': {
        'example_setting': True,
    },
}

REDIS = {
    'tasks': {
        'host': 'redis',
        'port': 6379,
        'database': 0,
    }
}
