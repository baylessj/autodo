"""
Django settings for gettingstarted project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys
import django_heroku
import logging
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BACKEND_DIR = BASE_DIR
FRONTEND_DIR = os.path.abspath(os.path.join(BACKEND_DIR, "frontend"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "CHANGE_ME!!!! (P.S. the SECRET_KEY environment variable will be used, if set, instead)."

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "True") == "True"
print(DEBUG)
sys.stdout.flush()

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "extra_views",
    "djmoney",
    "autodo.apps.AutodoConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "..", "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "main.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "..", "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTH_USER_MODEL = "autodo.User"

# Go to the home page after logging in rather than the account profile page
LOGIN_REDIRECT_URL = "/"

EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]
# Toggle sandbox mode (when running in DEBUG mode)
SENDGRID_SANDBOX_MODE_IN_DEBUG = False
# echo to stdout or any other file-like object that is passed to the backend via the stream kwarg.
SENDGRID_ECHO_TO_STDOUT = True
DEFAULT_FROM_EMAIL = "noreply@autodo.app"
SERVER_EMAIL = "noreply@autodo.app"


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, "..", "staticfiles")]
STATIC_ROOT = os.path.join(BACKEND_DIR, "..", "staticfiles")
STATIC_URL = "/static/"  # already declared in the default settings


def get_cache():
    import os

    try:
        servers = os.environ["MEMCACHIER_SERVERS"]
        username = os.environ["MEMCACHIER_USERNAME"]
        password = os.environ["MEMCACHIER_PASSWORD"]
        return {
            "default": {
                "BACKEND": "django.core.cache.backends.memcached.PyLibMCCache",
                # TIMEOUT is not the connection timeout! It's the default expiration
                # timeout that should be applied to keys! Setting it to `None`
                # disables expiration.
                "TIMEOUT": None,
                "LOCATION": servers,
                "OPTIONS": {
                    "binary": True,
                    "username": username,
                    "password": password,
                    "behaviors": {
                        # Enable faster IO
                        "no_block": True,
                        "tcp_nodelay": True,
                        # Keep connection alive
                        "tcp_keepalive": True,
                        # Timeout settings
                        "connect_timeout": 2000,  # ms
                        "send_timeout": 750 * 1000,  # us
                        "receive_timeout": 750 * 1000,  # us
                        "_poll_timeout": 2000,  # ms
                        # Better failover
                        "ketama": True,
                        "remove_failed": 1,
                        "retry_timeout": 2,
                        "dead_timeout": 30,
                    },
                },
            }
        }
    except:
        return {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}


CACHES = get_cache()

CURRENCIES = ("USD",)

if not DEBUG:
    sentry_sdk.init(
        dsn=os.environ["SENTRY_DSN"],
        integrations=[
            DjangoIntegration(),
            LoggingIntegration(level=logging.INFO, event_level=logging.ERROR),
        ],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production,
        traces_sample_rate=1.0,
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
        # By default the SDK will try to use the SENTRY_RELEASE
        # environment variable, or infer a git commit
        # SHA as release, however you may want to set
        # something more human-readable.
        # release="myapp@1.0.0",
    )

django_heroku.settings(locals())
