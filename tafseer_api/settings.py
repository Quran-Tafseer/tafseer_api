import os
import environ
from django.utils.translation import ugettext_lazy as _

# Initialize environ
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env(DEBUG=(bool, False),)
env_file_path = os.path.join(BASE_DIR, '.env')
environ.Env.read_env(env_file_path)  # reading .env file

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party Apps
    'rest_framework',
    # Internal Apps
    'quran_text',
    'quran_tafseer',
    'docs',
    'opbeat.contrib.django',
]

PRE_MIDDLEWARE = env.list('PRE_MIDDLEWARE', default=[])

POST_MIDDLEWARE = env.list('POST_MIDDLEWARE', default=[])

MIDDLEWARE = PRE_MIDDLEWARE + [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
] + POST_MIDDLEWARE

MIDDLEWARE_CLASSES = env.list('MIDDLEWARE_CLASSES', default=[])

ROOT_URLCONF = 'tafseer_api.urls'

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

WSGI_APPLICATION = env('WSGI_APPLICATION', default='tafseer_api.wsgi.application')


DATABASES = {'default': env.db()}

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


LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', _('English')),
    ('ar', _('Arabic'))
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

OPBEAT = env.dict('OPBEAT', default={})

REST_FRAMEWORK_RENDERER = env.list('REST_FRAMEWORK_RENDERER', default=[])

REST_FRAMEWORK_PARSER = env.list('REST_FRAMEWORK_PARSER', default=[])

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ] + REST_FRAMEWORK_RENDERER,
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ] + REST_FRAMEWORK_PARSER
}
