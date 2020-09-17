"""
Base settings to build other settings files upon.
"""
#import os
from pathlib import Path
import environ
import datetime

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent  # base_new/
APPS_DIR = ROOT_DIR / "apps"
BASE_TEMPLATE_DIR = ROOT_DIR /"base_templates"
#EXTERNAL_BASE = ROOT_DIR.path("externals")
#EXTERNAL_LIBS_PATH = EXTERNAL_BASE.path("libs")
#EXTERNAL_APPS_PATH = EXTERNAL_BASE.path("apps")

env = environ.Env()

READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / ".env"))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', True)
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = 'UTC'
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(ROOT_DIR / "locale")]

# Site config
SITE_TITLE = 'Agile Design 2.0'
SITE_NAME = 'AD Blog'
SITE_ABOUT = 'Base design, django blog' 

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
#{% if cookiecutter.use_docker == "y" -%}
#DATABASES = {"default": env.db("DATABASE_URL")}
#{%- else %}
"""
DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres://localhost/base_new'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
"""
DATABASES = {
    'default': {
    	'ENGINE': 'django.db.backends.sqlite3',
    	'NAME': str(ROOT_DIR / 'db.sqlite3'),
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'ENGINE': 'django.db.backends.postgresql',
        #'NAME': 'base_new_blog5',
        #'NAME': 'contract',
        #'NAME': 'base_v_0.1.0',
        #'USER': 'postgres',
        #'PASSWORD': '',
        #'ATOMIC_REQUESTS': True,
    }
}


# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'config.urls'
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.humanize', # Handy template tags
    'django.contrib.admin',
    'django.contrib.sitemaps',
    "django.forms",
]
THIRD_PARTY_APPS = [
    'crispy_forms',
    #'rest_framework',
    #'haystack',
    #'sorl.thumbnail',
    #'django_filters',
    'allauth',
    'allauth.account',
    #'allauth.socialaccount',
    #'django_celery_beat',
    #'rest_framework',
    #'rest_framework.authtoken', 
    # other apps
    # for post
    # pages
    'robots',
]

LOCAL_APPS = [
    'users.apps.UsersAppConfig',
    'static_page',
    # Your stuff: custom apps go here
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {
    'sites': 'base_templates.contrib.sites.migrations'
}

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = 'users.User'
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = 'users:redirect'
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = 'account_login'

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
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

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #{%- if cookiecutter.use_whitenoise == 'y' %}
    'whitenoise.middleware.WhiteNoiseMiddleware',
    #{%- endif %}
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(BASE_TEMPLATE_DIR / "static")]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(BASE_TEMPLATE_DIR /  "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [str(BASE_TEMPLATE_DIR / "templates")],
        'OPTIONS': {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'utils.context_processors.settings_context',
            ],
        },
    },
]

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(BASE_TEMPLATE_DIR / "fixtures"),)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5


# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = 'admin/'
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [
    ("""David Gomez""", 'agiledesign2.0@gmail.com'),
]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": BASE_TEMPLATE_DIR / 'debug.log',
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console", "file"]},
}

#{% if cookiecutter.use_celery == 'y' -%}
# Celery
# ------------------------------------------------------------------------------
#if USE_TZ:
    # http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-timezone
    #CELERY_TIMEZONE = TIME_ZONE
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-broker_url
#CELERY_BROKER_URL = env("CELERY_BROKER_URL")
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_backend
#CELERY_RESULT_BACKEND = CELERY_BROKER_URL
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-accept_content
#CELERY_ACCEPT_CONTENT = ["json"]
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-task_serializer
#CELERY_TASK_SERIALIZER = "json"
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_serializer
#CELERY_RESULT_SERIALIZER = "json"
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-time-limit
# TODO: set to whatever value is adequate in your circumstances
#CELERY_TASK_TIME_LIMIT = 5 * 60
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-soft-time-limit
# TODO: set to whatever value is adequate in your circumstances
#CELERY_TASK_SOFT_TIME_LIMIT = 60
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#beat-scheduler
#CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

#{%- endif %}
# django-allauth
# ------------------------------------------------------------------------------
#ACCOUNT_ALLOW_REGISTRATION = env.bool('DJANGO_ACCOUNT_ALLOW_REGISTRATION', True)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
#ACCOUNT_AUTHENTICATION_METHOD = 'username'
# https://django-allauth.readthedocs.io/en/latest/configuration.html
#ACCOUNT_EMAIL_REQUIRED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
#ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# https://django-allauth.readthedocs.io/en/latest/configuration.html
#ACCOUNT_ADAPTER = 'users.adapters.AccountAdapter'
# https://django-allauth.readthedocs.io/en/latest/configuration.html
#SOCIALACCOUNT_ADAPTER = 'users.adapters.SocialAccountAdapter'

# django-compressor
# ------------------------------------------------------------------------------
# https://django-compressor.readthedocs.io/en/latest/quickstart/#installation
#INSTALLED_APPS += ["compressor"]
#STATICFILES_FINDERS += ["compressor.finders.CompressorFinder"]

#MENUS_CONF = 'post.menu.py'

#EMAIL_USE_TLS = True  
#EMAIL_HOST = 'smtp.gmail.com'  
#EMAIL_PORT = 587  
#EMAIL_HOST_USER = 'laike9m@gmail.com'  # this is my email address, use yours
#EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']   # set environ yourself

#ADMINS = (
#    ('your_name', 'your_email'),   # email will be sent to your_email
#)

#MANAGERS = ADMINS

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
"""
HAYSTACK_CONNECTIONS = {
    'default_en-us': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': str(APPS_DIR.path('tmp/whoosh_index_en')),
    },
}
"""
"""
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr',
        'INCLUDE_SPELLING': True,
    },
}
"""
"""
HAYSTACK_CONNECTIONS['default'] = \
    HAYSTACK_CONNECTIONS[f'default_{LANGUAGE_CODE}']

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# django-rest-framework
# -------------------------------------------------------------------------------
# django-rest-framework - https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    'DATE_INPUT_FORMATS': ['%d/%m/%Y'], # ['%d/%m/%Y'] # [('%d/%m/%Y'),]
    'DEFAULT_PAGINATION_CLASS': 
        'rest_framework.pagination.PageNumberPagination',
        #'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend', 
        'rest_framework.filters.OrderingFilter', 
        'rest_framework.filters.SearchFilter', 
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        #'rest_framework.authentication.TokenAuthentication',
        #'rest_framework.authentication.BasicAuthentication',
    ),
}
"""

# Your stuff...
# ------------------------------------------------------------------------------
#ROBOTS_SITEMAP_URLS = [
#    'http://www.example.com/sitemap.xml',
#]
#ROBOTS_SITEMAP_VIEW_NAME = ''
#ROBOTS_USE_HOST = False
#ROBOTS_USE_SCHEME_IN_HOST = True
#ROBOTS_CACHE_TIMEOUT = 60*60*24

# Django-Meta
# ------------------------------------------------------------------------------
#META_SITE_PROTOCOL = 'http'
#META_USE_SITES = True
#META_SITE_NAME = 'agiledesign blog'
#META_SITE_DOMAIN = ''
# META_IMAGE_URL
#META_USE_OG_PROPERTIES = True
#META_USE_TWITTER_PROPERTIES = True
#META_USE_TITLE_TAG = True
#META_USE_SITES = True

# Django-Analytical
# ------------------------------------------------------------------------------
#GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-116517635-3'
#GOOGLE_ANALYTICS_JS_PROPERTY_ID = 'UA-116517635-3'