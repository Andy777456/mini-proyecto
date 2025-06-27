"""
ASGI config for django_todo project.

Expone el callable ASGI como una variable a nivel de módulo llamada ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Establece la variable de entorno para el módulo de configuración de Django.
# Esto le dice a Django dónde encontrar la configuración del proyecto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_todo.settings')

# Obtiene la aplicación ASGI por defecto para tu proyecto.
# Esta es la interfaz que los servidores ASGI (como Daphne o Uvicorn) usarán para comunicarse con tu aplicación Django.
application = get_asgi_application()
