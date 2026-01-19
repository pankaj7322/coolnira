from pathlib import Path
import os
SECRET_KEY = 'django-insecure-1234567890-change-this'

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECRET_KEY = os.getenv('SECRET_KEY')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # REQUIRED
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # REQUIRED
    'django.contrib.messages.middleware.MessageMiddleware',     # REQUIRED
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.accounts.apps.AccountsConfig',
    'apps.buyers.apps.BuyersConfig',
    'apps.customers.apps.CustomersConfig',
    'apps.services.apps.ServicesConfig',
]

AUTH_USER_MODEL = 'accounts.User'
ROOT_URLCONF = 'core.urls'
STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / 'static']


STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

WSGI_APPLICATION = 'core.wsgi.application'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',   # REQUIRED
                'django.contrib.auth.context_processors.auth',  # REQUIRED
                'django.contrib.messages.context_processors.messages',  # REQUIRED
            ],
        },
    },
]
