"""
WSGI config for portfolio_hub — PythonAnywhere version.

Copy this file's content into the WSGI configuration file that
PythonAnywhere shows in the Web tab, replacing whatever is there.
Remember to update the paths below to match your username.
"""

import os
import sys

# ── 1. Add your project to the Python path ───────────────────────────────────
# Replace 'yourusername' with your actual PythonAnywhere username
path = '/home/yourusername/portfolio_hub'
if path not in sys.path:
    sys.path.insert(0, path)

# ── 2. Set secrets (or use python-dotenv — see below) ────────────────────────
os.environ['SECRET_KEY'] = 'REPLACE-WITH-YOUR-ACTUAL-SECRET-KEY'

# ── 2b. Alternative: load from .env file with python-dotenv ──────────────────
# from dotenv import load_dotenv
# load_dotenv(os.path.join(path, '.env'))

# ── 3. Point to the production settings module ───────────────────────────────
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_hub.deployment')

# ── 4. Hand off to Django ─────────────────────────────────────────────────────
from django.core.wsgi import get_wsgi_application  # noqa: E402
application = get_wsgi_application()
