# -*- coding: utf-8 -*-

"""
Django settings for test_project project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from __future__ import unicode_literals

import os
from logging.handlers import SysLogHandler

from modoboa.test_settings import *  # noqa

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "w537@nm@5n)=+e%-7*z-jxf21a#0k%uv^rbu**+cj4=_u57e(8"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = "DEBUG" in os.environ

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

SITE_ID = 1

# Security settings

X_FRAME_OPTIONS = "SAMEORIGIN"

# Application definition

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "reversion",
    "ckeditor",
    "ckeditor_uploader",
    "rest_framework",
    "rest_framework.authtoken",
)

# A dedicated place to register Modoboa applications
# Do not delete it.
# Do not change the order.
MODOBOA_APPS = (
    "modoboa",
    "modoboa.core",
    "modoboa.lib",
    "modoboa.admin",
    "modoboa.transport",
    "modoboa.relaydomains",
    "modoboa.limits",
    "modoboa.parameters",
    "modoboa.dnstools",
    # Modoboa extensions here.
    "modoboa_amavis",
)

INSTALLED_APPS += MODOBOA_APPS

AUTH_USER_MODEL = "core.User"

MIDDLEWARE = (
    "x_forwarded_for.middleware.XForwardedForMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "modoboa.core.middleware.LocalConfigMiddleware",
    "modoboa.lib.middleware.AjaxLoginRedirect",
    "modoboa.lib.middleware.CommonExceptionCatcher",
    "modoboa.lib.middleware.RequestCatcherMiddleware",
)

AUTHENTICATION_BACKENDS = (
    # 'modoboa.lib.authbackends.LDAPBackend',
    # 'modoboa.lib.authbackends.SMTPBackend',
    "django.contrib.auth.backends.ModelBackend",
)

# SMTP authentication
# AUTH_SMTP_SERVER_ADDRESS = 'localhost'
# AUTH_SMTP_SERVER_PORT = 25
# AUTH_SMTP_SECURED_MODE = None  # 'ssl' or 'starttls' are accepted


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
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "modoboa.core.context_processors.top_notifications",
            ],
            "debug": TEMPLATE_DEBUG,
        },
    },
]

ROOT_URLCONF = "test_project.urls"

WSGI_APPLICATION = "test_project.wsgi.application"


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = "/sitestatic/"
STATIC_ROOT = os.path.join(BASE_DIR, "sitestatic")
STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, '..', 'modoboa', 'bower_components'),
)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Rest framework settings

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
}

# Modoboa settings
# MODOBOA_CUSTOM_LOGO = os.path.join(MEDIA_URL, "custom_logo.png")

# DOVECOT_LOOKUP_PATH = ('/path/to/dovecot', )

MODOBOA_API_URL = "https://api.modoboa.org/1/"

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # NOQA:E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # NOQA:E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # NOQA:E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # NOQA:E501
    },
    {
        "NAME": "modoboa.core.password_validation.ComplexityValidator",
        "OPTIONS": {
            "upper": 1,
            "lower": 1,
            "digits": 1,
            "specials": 0
        }
    },
]

# CKeditor

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_BROWSE_SHOW_DIRS = True

CKEDITOR_ALLOW_NONIMAGE_FILES = False

CKEDITOR_CONFIGS = {
    "default": {
        "allowedContent": True,
        "toolbar": "Modoboa",
        "width": None,
        "toolbar_Modoboa": [
            ["Bold", "Italic", "Underline"],
            ["JustifyLeft", "JustifyCenter", "JustifyRight", "JustifyBlock"],
            ["BidiLtr", "BidiRtl", "Language"],
            ["NumberedList", "BulletedList", "-", "Outdent", "Indent"],
            ["Undo", "Redo"],
            ["Link", "Unlink", "Anchor", "-", "Smiley"],
            ["TextColor", "BGColor", "-", "Source"],
            ["Font", "FontSize"],
            ["Image", ],
            ["SpellChecker"]
        ],
    },
}

# Logging configuration

LOGGING = {
    "version": 1,
    "formatters": {
        "syslog": {
            "format": "%(name)s: %(levelname)s %(message)s"
        },
    },
    "handlers": {
        "syslog-auth": {
            "class": "logging.handlers.SysLogHandler",
            "facility": SysLogHandler.LOG_AUTH,
            "formatter": "syslog"
        },
        "modoboa": {
            "class": "modoboa.core.loggers.SQLHandler",
        }
    },
    "loggers": {
        "modoboa.auth": {
            "handlers": ["syslog-auth", "modoboa"],
            "level": "INFO",
            "propagate": False
        },
        "modoboa.admin": {
            "handlers": ["modoboa"],
            "level": "INFO",
            "propagate": False
        }
    }
}

# Load settings from extensions
try:
    from modoboa_amavis import settings as modoboa_amavis_settings
    modoboa_amavis_settings.apply(globals())
except AttributeError:
    from modoboa_amavis.settings import *  # noqa


MIGRATION_MODULES = {
    "modoboa_amavis": None
}

TEST_RUNNER = "modoboa_amavis.test_runners.UnManagedModelTestRunner"

# We force sqlite backend for tests because the generated database is
# not the same as the one provided by amavis...
DATABASES.update({  # noqa
    "amavis": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "amavis.db",
        "PORT": "",
        "ATOMIC_REQUESTS": True,
    },
})
# sqlite defaults to UTF-8
AMAVIS_DEFAULT_DATABASE_ENCODING = "UTF-8"
