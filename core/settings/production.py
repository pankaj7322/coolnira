from .base import *
import os
from pathlib import Path

DEBUG = False

ALLOWED_HOSTS = ['coolnira.in', 'www.coolnira.in', 'coolnira.onrender.com']

# Whitenoise for serving static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Static files (CSS, JS, Images)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
