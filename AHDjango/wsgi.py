"""
WSGI config for AHDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import wsgiref.simple_server

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AHDjango.settings')

application = get_wsgi_application()

if __name__ == '__main__':
    server = wsgiref.simple_server.make_server(host='localhost', app=application, port=8888)
    server.serve_forever()