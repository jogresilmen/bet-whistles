"""
Django settings for sportbettingtips project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import environ
import os

from django.utils.translation import gettext_lazy as _
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# environ settings
ENVIROMENT = environ.Env()  # set default values and casting
environ.Env.read_env()  # reading .env file

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-dl61li803a0=77_$nw*_)gtphzj@2^sfs74hte^1fum!$b2*b^'
SECRET_KEY = ENVIROMENT("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENVIROMENT.bool('DEBUG', default= False)

# ALLOWED_HOSTS = ENVIROMENT.list('ALLOWED_HOSTS',default=[])
ALLOWED_HOSTS=['127.0.0.1','localhost',]


# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    
    "django.contrib.sites",
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sitemaps",
    "django.contrib.humanize",
    
    # propios
    
    'app.api',
    'app.config',
    'app.main',
    'app.usercustom',
    'app.forecaster',
    'app.client',
    "app.dominio",
    

    # externo
    "simple_history",
    "app.rosetta",
    "bootstrap_datepicker_plus",
    "ckeditor",
    "dal",
    "dal_select2",
    "bootstrap4",
    
    
    
]
SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'sportbettingtips.urls'
CKEDITOR_UPLOAD_PATH = "uploads/"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        # 'APP_DIRS': True,
        'OPTIONS': {
            "loaders": ["django.template.loaders.app_directories.Loader"],
            'context_processors': [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django_settings_export.settings_export",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.csrf",
            ],
        },
    },
]

WSGI_APPLICATION = 'sportbettingtips.wsgi.application'

EMAIL_BACKEND = ENVIROMENT("EMAIL_BACKEND")
EMAIL_HOST = ENVIROMENT("EMAIL_HOST")
EMAIL_PORT = ENVIROMENT("EMAIL_PORT")
EMAIL_HOST_USER = ENVIROMENT("EMAIL_USER")
EMAIL_HOST_PASSWORD = ENVIROMENT("EMAIL_PASSWORD")
EMAIL_USE_TLS = True

""" Esta configuraci??n hace disponible todas esta variables en cualquier
plantilla
"""

PROJECT_NAME = ENVIROMENT("PROJECT_NAME")
SLOGAN = ENVIROMENT("SLOGAN")
PREFIX = ENVIROMENT("PREFIX")
SUFIX = ENVIROMENT("SUFIX")
VERSION = ENVIROMENT("VERSION")
INITIAL_A = ENVIROMENT("INITIAL_A")
INITIAL_B = ENVIROMENT("INITIAL_B")
YEA = ENVIROMENT("YEA")

SETTINGS_EXPORT = [
    'PROJECT_NAME',
    'SLOGAN',
    'PREFIX',
    'SUFIX',
    'VERSION',
    'INITIAL_A',
    'INITIAL_B',
    'YEA'
]


""" Esta configuraci??n define el modelo personalizado para auth.user. Tambien
establece las rutas para algunas funciones.
"""
AUTH_USER_MODEL = "usercustom.UserCustom"
LOGIN_URL = "usercustom:login"
LOGOUT_REDIRECT_URL = "usercustom:login"
LOGIN_REDIRECT_URL = "usercustom:profile"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "USER": ENVIROMENT("DBUSER"),
        "NAME": ENVIROMENT("DBNAME"),
        "PASSWORD": ENVIROMENT("DBPASSWORD"),
        "HOST": ENVIROMENT("DBHOST"),
        "DATABASE_PORT": ENVIROMENT("DBPORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en"
TIME_ZONE = "America/Caracas"
# Restricts languages
# Al usar lenguages del tipo en-us. es-ve, fr-ca no funciona la traducci??n
LANGUAGES = [("en", _("English")), ("es", _("Spanish")), ("fr", _("French"))]
# Where Django looks for translation files
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]
USE_I18N = True
USE_L10N = True
USE_TZ = True

ROSETTA_EXCLUDED_APPLICATIONS = (
    "dal_select2",
    "django_extensions",
    "mptt",
    "zinnia",
    "django_comments",
)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

MEDIA_URL = "/media/"
MEDIA_ROOT = "media"
STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
