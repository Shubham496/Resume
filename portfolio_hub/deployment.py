"""
Production settings for portfolio_hub.
Used on PythonAnywhere via DJANGO_SETTINGS_MODULE=portfolio_hub.deployment
"""

import os

from .settings import *  # noqa: F401, F403

# ---------------------------------------------------------------------------
# Security
# ---------------------------------------------------------------------------
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']          # must be set in WSGI / env

ALLOWED_HOSTS = [
    'yourusername.pythonanywhere.com',          # ← replace with your username
]

CSRF_TRUSTED_ORIGINS = [
    'https://yourusername.pythonanywhere.com',  # ← replace with your username
]

# ---------------------------------------------------------------------------
# HTTPS / cookie hardening
# ---------------------------------------------------------------------------
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# ---------------------------------------------------------------------------
# Static & media
# ---------------------------------------------------------------------------
STATIC_ROOT = BASE_DIR / 'staticfiles'         # noqa: F405
MEDIA_ROOT = BASE_DIR / 'media'                # noqa: F405

# ---------------------------------------------------------------------------
# Cache (file-based so it survives reloads on free tier)
# ---------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR / '.cache',        # noqa: F405
    }
}
