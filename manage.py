#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Ejecuta tareas administrativas de Django."""
    # Establece la variable de entorno DJANGO_SETTINGS_MODULE.
    # Esto le dice a Django qué archivo de configuración usar para el proyecto.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_todo.settings')
    try:
        # Intenta importar execute_from_command_line de Django.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Captura un error si Django no está instalado o no está configurado correctamente.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Ejecuta el comando de Django pasado como argumento desde la línea de comandos.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
