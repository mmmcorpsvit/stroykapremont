import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

API_GOOGLE_KEY = 'AIzaSyCDv-y99GoYalDSxIPs0FfgS_B8KLyaAVs'
API_GOOGLE_MAP_IFRAME_LINK = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1124.8314857577398!2d37.854732204779474!3d55.677460672749994!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x414ab66c1530f471%3A0xdb222797532ba18a!2z0J_RgNC40LLQvtC70YzQvdCw0Y8g0YPQuy4sIDcwINC60L7RgNC_0YPRgSAxLCDQnNC-0YHQutCy0LAsINCg0L7RgdGW0Y8sIDEwOTQzMQ!5e0!3m2!1suk!2sua!4v1519066611059'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ['sdfsdf', False]
DEBUG = True

# ALLOWED_HOSTS = ['192.168.137.1']
ALLOWED_HOSTS = ['127.0.0.1']

SITE_NAME = 'ООО "Стройкапремонт"'


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'mptt',
    'adminsortable',

    'easy_thumbnails',
    'filer',
    'tinymce',

    'landing_page',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.cache.CacheMiddleware',

    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'stroykapremont.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',

                'django_settings_export.settings_export',

            ],
        },
    },
]

WSGI_APPLICATION = 'stroykapremont.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'en'
LANGUAGE_CODE = 'ru'
# LANGUAGE_CODE = 'ru-RU'

LANGUAGES = [
  ('ru', _('Russian')),
  ('en', _('English')),
]

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SETTINGS_EXPORT = [
    'SITE_NAME',
    'API_GOOGLE_KEY',
    'API_GOOGLE_MAP_IFRAME_LINK',
]
