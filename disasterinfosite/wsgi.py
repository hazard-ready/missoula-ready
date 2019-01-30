"""
WSGI config for disasterinfosite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "disasterinfosite.settings")
wsgi_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(wsgi_dir, '/venv/lib/python3.5/site-packages'))
sys.path.append(wsgi_dir)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
