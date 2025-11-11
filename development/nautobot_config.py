import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

GIT_ROOT = os.path.join(BASE_DIR, "git")
JOBS_ROOT = os.path.join(BASE_DIR, "jobs")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = "/opt/nautobot/static"

METRICS_ENABLED = True
STORAGE_BACKEND = "nautobot.core.storage.LocalStorage"
VERSION = "2.4.0"  # match your exact Nautobot version

SECRET_KEY = "9.V$@Kxkc@@Kd@z<a/=.J-Y;rYc79<y@](9o9(L(*sS)Q+ud5P"
TIME_ZONE = "UTC"
USE_TZ = True
DEBUG = True  # Set True for local dev only
LOGIN_URL = "login"
ALLOWED_HOSTS = ["*"]  # Adjust for your environment

# Time zone and localization
TIME_ZONE = "UTC"
USE_TZ = True
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

REDIS = {
    'tasks': {
        'host': 'redis',
        'port': 6379,
        'database': 0,
    }
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "django_celery_results",
    "rest_framework",
    "django_celery_beat",
    "silk",
    "constance",
    "nautobot.core",
    "nautobot.extras",
    "nautobot.dcim",
    "nautobot.ipam",
    "nautobot.tenancy",
    "nautobot.users",
    "nautobot.virtualization",
    "nautobot.circuits",
    "nautobot.cloud",
    "nautobot.wireless",
]
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
EVENT_BROKERS = {}
# Background task processing queue name for Celery
CELERY_TASK_DEFAULT_QUEUE = "default"
ALLOWED_URL_SCHEMES = ["http", "https", "ftp", "ftps", "ssh", "telnet"]


JOB_FILE_IO_STORAGE = "django.core.files.storage.FileSystemStorage"
STORAGE_BACKEND = "django.core.files.storage.FileSystemStorage"
MAINTENANCE_MODE = False
ROOT_URLCONF = "nautobot.core.urls"
METRICS_AUTHENTICATED = False





STORAGE_CONFIG = {
    "local": {
        "backend": STORAGE_BACKEND,
        "media_root": MEDIA_ROOT,
    }
}

# Authentication backends
AUTHENTICATION_BACKENDS = [
    "nautobot.core.authentication.ObjectPermissionBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# Custom user model (adjust if you use a custom one)
# AUTH_USER_MODEL = "users.User"  # Uncomment if using custom user

# Middleware stack required by Django and Nautobot admin
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Django templates setting needed for admin
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "nautobot.core.context_processors.settings",  # Add this instead

            ],
        },
    },
]


# Nautobot core settings
MAINTENANCE_MODE = False
METRICS_ENABLED = True
METRICS_AUTHENTICATED = False

# Must have for valid Django URL resolution
ROOT_URLCONF = "nautobot.core.urls"

# Proper SANITIZER_PATTERNS: list of tuples of (compiled_regex, replacement_str)
SANITIZER_PATTERNS = [
    (re.compile(r"(?i)password"), "[PASSWORD]"),
    (re.compile(r"(?i)secret"), "[SECRET]"),
    (re.compile(r"(?i)token"), "[TOKEN]"),
    (re.compile(r"(?i)key"), "[KEY]"),
    (re.compile(r"(?i)credential"), "[CREDENTIAL]"),
    (re.compile(r"(?i)private_key"), "[PRIVATE_KEY]"),
]

# Email backend for local testing - adjust for production
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Additional recommended security settings can be added here...
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
INSTALLATION_METRICS_ENABLED = False
CONTENT_TYPE_CACHE_TIMEOUT = 60 * 60 * 24  # e.g. 86400 seconds = 24 hours

BRANDING_FILEPATHS = {
    "favicon": None,
    "logo": None,
    "login_logo": None,
    "icon": None,
}

BANNER_TOP = ""
BANNER_BOTTOM = ""
BANNER_LOGIN = ""

CONSTANCE_CONFIG = {
    "BANNER_TOP": ("", "Top banner text"),
    "BANNER_BOTTOM": ("", "Bottom banner text"),
    "BANNER_LOGIN": ("", "Login banner text"),
}

LOGIN_REDIRECT_URL="home"
LOGOUT_REDIRECT_URL="login"
HOME_URL="home"
