"""
WSGI config for pokeapi_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

path = "/home/<tu_nombre_de_usuario>/<ruta_a_tu_proyecto>"
if path not in sys.path:
    sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] = "pokeapi_project.settings"

application = get_wsgi_application()
