import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Path to your .env file
dotenv_path = os.path.join(Path(__file__).resolve().parent.parent.parent, '.env')

load_dotenv(dotenv_path)

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = os.getenv('DJANGO_DEBUG', False)

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS')
if ALLOWED_HOSTS and isinstance(ALLOWED_HOSTS, str):
    ALLOWED_HOSTS = ALLOWED_HOSTS.split(",")
else:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

CORS_ORIGIN_WHITELIST = os.getenv('DJANGO_CORS_ORIGIN_WHITELIST')
if CORS_ORIGIN_WHITELIST and isinstance(CORS_ORIGIN_WHITELIST, str):
    CORS_ORIGIN_WHITELIST = CORS_ORIGIN_WHITELIST.split(",")
else:
    CORS_ORIGIN_WHITELIST = ["http://localhost:3000", "http://127.0.0.1"]

CSRF_TRUSTED_ORIGINS = os.getenv('DJANGO_CSRF_TRUSTED_ORIGINS')
if CSRF_TRUSTED_ORIGINS and isinstance(CSRF_TRUSTED_ORIGINS, str):
    CSRF_TRUSTED_ORIGINS = CSRF_TRUSTED_ORIGINS.split(",")
else:
    CSRF_TRUSTED_ORIGINS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django rest
    'rest_framework',
    'rest_framework.authtoken',
    # auth

    "allauth",  # If you want to add email confirmation or social login https://testdriven.io/blog/django-rest-auth/
    "allauth.account",
    "dj_rest_auth",
    "dj_rest_auth.registration",

    # apps
    'core',
    'todo',
    'authentication',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'postgres'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.getenv('POSTGRES_HOST', 'postgres'),
        'PORT': os.getenv('POSTGRES_PORT', 5432),
    }
}

# Password validation

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

# django rest_framework settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ]

}

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.getenv('TIME_ZONE', 'UTC')

USE_I18N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "mount/files/static")

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'
