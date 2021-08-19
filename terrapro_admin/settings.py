"""
Django settings for terrapro_admin project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@9a%a90@wyz%vmknay#wuz!@n6v6d)u)@kfkc#d^9t-z@b7ku9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Auth user
LOGIN_URL = 'account:login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'account:login'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_q',

    'account.apps.AccountConfig',
    'api.apps.ApiConfig',
    'post.apps.PostConfig',
    'city.apps.CityConfig',
    'branch.apps.BranchConfig',
    'report.apps.ReportConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'terrapro_admin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'terrapro_admin.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'terrapro',
        'HOST': '68.183.125.203',
        'PORT': 5432,
        'USER': 'terra_pro_user',
        'PASSWORD': 'Jfn7Fjrk!ds',
    },
    'qcluster': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'terrapro_cluster',
        'HOST': '68.183.125.203',
        'PORT': 5432,
        'USER': 'terra_pro_user',
        'PASSWORD': 'Jfn7Fjrk!ds',
    }
}

# Configure your Q cluster
# More details https://django-q.readthedocs.io/en/latest/configure.html
Q_CLUSTER = {
    'name': 'terrapro_admin',
    'workers': 3,
    'max_attempts': 1,
    'retry': 1200,
    'poll': 1,
    'orm': 'qcluster',  # Use Django's ORM + database for broker
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'resources/static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

BOT_TOKEN = '705057175:AAG74aoVTh6lutQAmKTpFDnhhVp8BWsEUxQ'
TELEGRAM_CHAT_ID = '-1001404598288'

SECONDS_BETWEEN_SENDING_MESSAGE = 2

LOG_DIR = os.path.join(BASE_DIR, 'log')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
          'format': '%(asctime)s; %(process)d; %(thread)d; %(levelname)s; %(name)s; %(message)s',  # noqa: E121, WPS323
          'datefmt': '%Y-%m-%d %H:%M:%S',  # noqa: WPS323
        },
    },
    'handlers': {
        'error.log': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
        'debug.log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'debug.log'),
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
        'info.log': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'debug.log'),
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        '': {
            'handlers': ['error.log', 'debug.log'],
        },
    },
}

DOCS_TMP_STORAGE = 'resources/tmp_storage/'

try:
    from .local_settings import *
except ImportError:
    pass
