#!/usr/bin/env bash

# Environment variables
#######################
IMAGEHOSTING_DEBUG=${IMAGEHOSTING_DEBUG:-"False"}
IMAGEHOSTING_SECRET_KEY=${IMAGEHOSTING_SECRET_KEY:-"change me!"}
IMAGEHOSTING_ALLOWED_HOSTS=${IMAGEHOSTING_ALLOWED_HOSTS:-"*"}

# Database
IMAGEHOSTING_DB_ENGINE=${IMAGEHOSTING_DB_ENGINE:-"django.db.backends.sqlite3"}
IMAGEHOSTING_DB_NAME=${IMAGEHOSTING_DB_NAME:-"db.sqlite3"}
IMAGEHOSTING_DB_PORT=${IMAGEHOSTING_DB_PORT:-"5432"}
IMAGEHOSTING_DB_HOST=${IMAGEHOSTING_DB_HOST:-"localhost"}
IMAGEHOSTING_DB_USER=${IMAGEHOSTING_DB_USER:-"postgres"}
IMAGEHOSTING_DB_PASS=${IMAGEHOSTING_DB_NAME:-"postgres"}

# Language and time
IMAGEHOSTING_LANGUAGE_CODE=${IMAGEHOSTING_LANGUAGE_CODE:-"ru-RU"}
IMAGEHOSTING_USE_I18N=${IMAGEHOSTING_USE_I18N:-"True"}
IMAGEHOSTING_USE_L10N=${IMAGEHOSTING_USE_L10N:-"True"}
IMAGEHOSTING_TIME_ZONE=${IMAGEHOSTING_TIME_ZONE:-"Europe/Moscow"}
IMAGEHOSTING_USE_TZ=${IMAGEHOSTING_USE_TZ:-"True"}

# Migrations
IMAGEHOSTING_MIGRATE=${IMAGEHOSTING_MIGRATE:-"False"}

# Listen string
IMAGEHOSTING_LISTEN_ADDR=${IMAGEHOSTING_LISTEN_ADDR:-"0.0.0.0:8080"}

cat > config/settings.py <<EOF
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = "${IMAGEHOSTING_SECRET_KEY}"
DEBUG = ${IMAGEHOSTING_DEBUG}
ALLOWED_HOSTS = ["${IMAGEHOSTING_ALLOWED_HOSTS}"]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'imagehosting',
]
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'imagehosting.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
WSGI_APPLICATION = 'config.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': "${IMAGEHOSTING_DB_ENGINE}",
        'NAME': "${IMAGEHOSTING_DB_NAME}",
        'HOST': "${IMAGEHOSTING_DB_HOST}",
        'PORT': "${IMAGEHOSTING_DB_PORT}",
        'USER': "${IMAGEHOSTING_DB_USER}",
        'PASSWORD': "${IMAGEHOSTING_DB_PASS}",
    }
}
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
LANGUAGE_CODE = "${IMAGEHOSTING_LANGUAGE_CODE}"
USE_I18N = ${IMAGEHOSTING_USE_I18N}
TIME_ZONE = "${IMAGEHOSTING_TIME_ZONE}"
USE_L10N = ${IMAGEHOSTING_USE_L10N}
USE_TZ = ${IMAGEHOSTING_USE_TZ}
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
EOF

if [[ ${IMAGEHOSTING_MIGRATE} == "True" ]]; then
    python manage.py makemigrations
    python manage.py migrate
fi

gunicorn --threads 2 config.wsgi:application --bind ${IMAGEHOSTING_LISTEN_ADDR} -t 60 --max-requests 200
