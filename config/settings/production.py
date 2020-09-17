#{% if cookiecutter.use_sentry == 'y' -%}
#import logging

#import sentry_sdk
#from sentry_sdk.integrations.django import DjangoIntegration
#from sentry_sdk.integrations.logging import LoggingIntegration
#{%- if cookiecutter.use_celery == 'y' %}
#from sentry_sdk.integrations.celery import CeleryIntegration
#{% endif %}

#{% endif -%}
from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env('DJANGO_SECRET_KEY')
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['*'])

# DATABASES
# ------------------------------------------------------------------------------
DATABASES['default'] = env.db('DATABASE_URL')  # noqa F405
DATABASES['default']['ATOMIC_REQUESTS'] = True  # noqa F405
DATABASES['default']['CONN_MAX_AGE'] = env.int('CONN_MAX_AGE', default=60)  # noqa F405
"""
# Postgres
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres:@postgres:5432/postgres',
        conn_max_age=int(os.getenv('POSTGRES_CONN_MAX_AGE', 600))
    )
}
"""
# CACHES
# ------------------------------------------------------------------------------
"""
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': env('REDIS_URL'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            # Mimicing memcache behavior.
            # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
            'IGNORE_EXCEPTIONS': True,
        }
    }
}
"""
# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)
#{% if cookiecutter.cloud_provider != 'None' -%}
# STORAGES
# ------------------------------------------------------------------------------
# https://django-storages.readthedocs.io/en/latest/#installation
#INSTALLED_APPS += ["storages"]  # noqa F405
#{%- endif -%}
#{% if cookiecutter.cloud_provider == 'AWS' %}
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
#AWS_ACCESS_KEY_ID = env("DJANGO_AWS_ACCESS_KEY_ID")
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
#AWS_SECRET_ACCESS_KEY = env("DJANGO_AWS_SECRET_ACCESS_KEY")
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
#AWS_STORAGE_BUCKET_NAME = env("DJANGO_AWS_STORAGE_BUCKET_NAME")
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
#AWS_QUERYSTRING_AUTH = False
# DO NOT change these unless you know what you're doing.
#_AWS_EXPIRY = 60 * 60 * 24 * 7
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
#AWS_S3_OBJECT_PARAMETERS = {
#    "CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate"
#}
#  https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
#AWS_DEFAULT_ACL = None
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
#AWS_S3_REGION_NAME = env("DJANGO_AWS_S3_REGION_NAME", default=None)
#{% elif cookiecutter.cloud_provider == 'GCP' %}
#GS_BUCKET_NAME = env("DJANGO_GCP_STORAGE_BUCKET_NAME")
#GS_DEFAULT_ACL = "publicRead"
#{% endif -%}

#{% if cookiecutter.cloud_provider != 'None' or cookiecutter.use_whitenoise == 'y' -%}
# STATIC
# ------------------------
#{% endif -%}
#{% if cookiecutter.use_whitenoise == 'y' -%}
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
#{% elif cookiecutter.cloud_provider == 'AWS' -%}
#STATICFILES_STORAGE = "{{cookiecutter.project_slug}}.utils.storages.StaticRootS3Boto3Storage"
#COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"
#STATIC_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/"
#{% elif cookiecutter.cloud_provider == 'GCP' -%}
#STATICFILES_STORAGE = "{{cookiecutter.project_slug}}.utils.storages.StaticRootGoogleCloudStorage"
#COLLECTFAST_STRATEGY = "collectfast.strategies.gcloud.GoogleCloudStrategy"
#STATIC_URL = f"https://storage.googleapis.com/{GS_BUCKET_NAME}/static/"
#{% endif -%}

# MEDIA
# ------------------------------------------------------------------------------
#{%- if cookiecutter.cloud_provider == 'AWS' %}
#DEFAULT_FILE_STORAGE = "{{cookiecutter.project_slug}}.utils.storages.MediaRootS3Boto3Storage"
#MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/"
#{%- elif cookiecutter.cloud_provider == 'GCP' %}
#DEFAULT_FILE_STORAGE = "{{cookiecutter.project_slug}}.utils.storages.MediaRootGoogleCloudStorage"
#MEDIA_URL = f"https://storage.googleapis.com/{GS_BUCKET_NAME}/media/"
#{%- endif %}

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES[0]['OPTIONS']['loaders'] = [  # noqa F405
#TEMPLATES[-1]["OPTIONS"]["loaders"] = [  # type: ignore[index] # noqa F405
    (
        'django.template.loaders.cached.Loader',
        [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]
    ),
]

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = env(
    'DJANGO_DEFAULT_FROM_EMAIL',
    default='base <noreply@example.com>'
)
# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env('DJANGO_EMAIL_SUBJECT_PREFIX', default='[Django Blog]')

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL regex.
ADMIN_URL = env('DJANGO_ADMIN_URL')


# Anymail
# ------------------------------------------------------------------------------
# https://anymail.readthedocs.io/en/stable/installation/#installing-anymail
INSTALLED_APPS += ["anymail"]  # noqa F405
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
#{%- if cookiecutter.mail_service == 'Mailgun' %}
# https://anymail.readthedocs.io/en/stable/esps/mailgun/
#EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
#ANYMAIL = {
#    "MAILGUN_API_KEY": env("MAILGUN_API_KEY"),
#    "MAILGUN_SENDER_DOMAIN": env("MAILGUN_DOMAIN"),
#    "MAILGUN_API_URL": env("MAILGUN_API_URL", default="https://api.mailgun.net/v3"),
#}
#{%- elif cookiecutter.mail_service == 'Amazon SES' %}
# https://anymail.readthedocs.io/en/stable/esps/amazon_ses/
#EMAIL_BACKEND = "anymail.backends.amazon_ses.EmailBackend"
#ANYMAIL = {}
#{%- elif cookiecutter.mail_service == 'Mailjet' %}
# https://anymail.readthedocs.io/en/stable/esps/mailjet/
#EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
#ANYMAIL = {
#    "MAILJET_API_KEY": env("MAILJET_API_KEY"),
#    "MAILJET_SECRET_KEY": env("MAILJET_SECRET_KEY"),
#    "MAILJET_API_URL": env("MAILJET_API_URL", default="https://api.mailjet.com/v3"),
#}
#{%- elif cookiecutter.mail_service == 'Mandrill' %}
# https://anymail.readthedocs.io/en/stable/esps/mandrill/
#EMAIL_BACKEND = "anymail.backends.mandrill.EmailBackend"
#ANYMAIL = {
#    "MANDRILL_API_KEY": env("MANDRILL_API_KEY"),
#    "MANDRILL_API_URL": env(
#        "MANDRILL_API_URL", default="https://mandrillapp.com/api/1.0"
#    ),
#}
#{%- elif cookiecutter.mail_service == 'Postmark' %}
# https://anymail.readthedocs.io/en/stable/esps/postmark/
#EMAIL_BACKEND = "anymail.backends.postmark.EmailBackend"
#ANYMAIL = {
#    "POSTMARK_SERVER_TOKEN": env("POSTMARK_SERVER_TOKEN"),
#    "POSTMARK_API_URL": env("POSTMARK_API_URL", default="https://api.postmarkapp.com/"),
#}
#{%- elif cookiecutter.mail_service == 'Sendgrid' %}
# https://anymail.readthedocs.io/en/stable/esps/sendgrid/
#EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
#ANYMAIL = {
#    "SENDGRID_API_KEY": env("SENDGRID_API_KEY"),
#    "SENDGRID_GENERATE_MESSAGE_ID": env("SENDGRID_GENERATE_MESSAGE_ID"),
#    "SENDGRID_MERGE_FIELD_FORMAT": env("SENDGRID_MERGE_FIELD_FORMAT"),
#    "SENDGRID_API_URL": env("SENDGRID_API_URL", default="https://api.sendgrid.com/v3/"),
#}
#{%- elif cookiecutter.mail_service == 'SendinBlue' %}
# https://anymail.readthedocs.io/en/stable/esps/sendinblue/
#EMAIL_BACKEND = "anymail.backends.sendinblue.EmailBackend"
#ANYMAIL = {
#    "SENDINBLUE_API_KEY": env("SENDINBLUE_API_KEY"),
#    "SENDINBLUE_API_URL": env(
#        "SENDINBLUE_API_URL", default="https://api.sendinblue.com/v3/"
#    ),
#}
#{%- elif cookiecutter.mail_service == 'SparkPost' %}
# https://anymail.readthedocs.io/en/stable/esps/sparkpost/
#EMAIL_BACKEND = "anymail.backends.sparkpost.EmailBackend"
#ANYMAIL = {
#    "SPARKPOST_API_KEY": env("SPARKPOST_API_KEY"),
#    "SPARKPOST_API_URL": env(
#        "SPARKPOST_API_URL", default="https://api.sparkpost.com/api/v1"
#    ),
#}
#{%- elif cookiecutter.mail_service == 'Other SMTP' %}
# https://anymail.readthedocs.io/en/stable/esps
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
ANYMAIL = {}
#{%- endif %}

#{% if cookiecutter.use_compressor == 'y' -%}
# django-compressor
# ------------------------------------------------------------------------------
# https://django-compressor.readthedocs.io/en/latest/settings/#django.conf.settings.COMPRESS_ENABLED
#COMPRESS_ENABLED = env.bool("COMPRESS_ENABLED", default=True)
# https://django-compressor.readthedocs.io/en/latest/settings/#django.conf.settings.COMPRESS_STORAGE
#{%- if cookiecutter.cloud_provider == 'AWS' %}
#COMPRESS_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
#{%- elif cookiecutter.cloud_provider == 'GCP' %}
#COMPRESS_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
#{%- elif cookiecutter.cloud_provider == 'None' %}
COMPRESS_STORAGE = "compressor.storage.GzipCompressorFileStorage"
#{%- endif %}
# https://django-compressor.readthedocs.io/en/latest/settings/#django.conf.settings.COMPRESS_URL
COMPRESS_URL = STATIC_URL
#{% if cookiecutter.use_whitenoise == 'y' or cookiecutter.cloud_provider == 'None' %}  # noqa F405{% endif %}
#{%- if cookiecutter.use_whitenoise == 'y' %}
# https://django-compressor.readthedocs.io/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
COMPRESS_OFFLINE = True  # Offline compression is required when using Whitenoise
#{%- endif %}
# https://django-compressor.readthedocs.io/en/latest/settings/#django.conf.settings.COMPRESS_FILTERS
COMPRESS_FILTERS = {
    "css": [
        "compressor.filters.css_default.CssAbsoluteFilter",
        "compressor.filters.cssmin.rCSSMinFilter",
    ],
    "js": ["compressor.filters.jsmin.JSMinFilter"],
}
#{% endif %}
#{%- if cookiecutter.use_whitenoise == 'n' -%}
# Collectfast
# ------------------------------------------------------------------------------
# https://github.com/antonagestam/collectfast#installation
#INSTALLED_APPS = ["collectfast"] + INSTALLED_APPS  # noqa F405
#{% endif %}

# Gunicorn
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['gunicorn']  # noqa F405

# LOGGING
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# more details on how to customize your logging configuration.
#{% if cookiecutter.use_sentry == 'n' -%}
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See https://docs.djangoproject.com/en/dev/topics/logging for
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_TEMPLATE_DIR / 'prod.log',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console', 'mail_admins', 'file'],
            'propagate': True
        }
    }
}
#{% else %}
"""
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.db.backends": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
        # Errors logged by the SDK itself
        "sentry_sdk": {"level": "ERROR", "handlers": ["console"], "propagate": False},
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}

# Sentry
# ------------------------------------------------------------------------------
#SENTRY_DSN = env("SENTRY_DSN")
#SENTRY_LOG_LEVEL = env.int("DJANGO_SENTRY_LOG_LEVEL", logging.INFO)

#sentry_logging = LoggingIntegration(
#    level=SENTRY_LOG_LEVEL,  # Capture info and above as breadcrumbs
#    event_level=logging.ERROR,  # Send errors as events
#)

#{%- if cookiecutter.use_celery == 'y' %}
#sentry_sdk.init(
#    dsn=SENTRY_DSN,
#    integrations=[sentry_logging, DjangoIntegration(), CeleryIntegration()],
#)
#{% else %}
#sentry_sdk.init(dsn=SENTRY_DSN, integrations=[sentry_logging, DjangoIntegration()])
#{% endif -%}
#{% endif %}
"""

# Your stuff...
# ------------------------------------------------------------------------------