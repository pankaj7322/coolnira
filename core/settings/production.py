from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.0.161','www.coolnira.in','coolnira.onrender.com']
# ALLOWED_HOSTS = ['www.coolnira.in','coolnira.onrender.com']

# WhiteNoise (recommended)
MIDDLEWARE.insert(
    1,
    'whitenoise.middleware.WhiteNoiseMiddleware'
)
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'