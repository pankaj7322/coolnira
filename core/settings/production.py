from .base import *

DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.0.161','www.coolina.in']
# WhiteNoise (recommended)
MIDDLEWARE.insert(
    1,
    'whitenoise.middleware.WhiteNoiseMiddleware'
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'