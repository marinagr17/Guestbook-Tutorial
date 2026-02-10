# build/app/django_tutorial/settings_test.py
# Configuración de Django para testing
# Importar todo de settings.py normal, pero sobrescribir BD

from .settings import *

# Usar SQLite en memoria para tests (mucho más rápido)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Desactivar migraciones lentas en tests (opcional pero recomendado)
class DisableMigrations:
    def __contains__(self, item):
        return True
    
    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()

# Logging mínimo en tests
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}

print("✓ Usando configuración de TESTING con SQLite en memoria")
