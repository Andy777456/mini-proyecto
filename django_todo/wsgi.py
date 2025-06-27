"""
WSGI config for django_todo project.

Expone el callable WSGI como una variable a nivel de módulo llamada ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Establece la variable de entorno para el módulo de configuración de Django.
# Esto le dice a Django dónde encontrar la configuración del proyecto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_todo.settings')

# Obtiene la aplicación WSGI por defecto para tu proyecto.
# Esta es la interfaz que los servidores WSGI (como Gunicorn o mod_wsgi) usarán para comunicarse con tu aplicación Django.
application = get_wsgi_application()
