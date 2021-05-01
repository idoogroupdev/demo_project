from .base import * # noqa
from apps.utils import get_secret

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': get_secret('DB_HOST'),
        'USER': get_secret('DB_USER'),
        'PASSWORD': get_secret('DEMO_PROJECT_DB_PASSWORD'),
        'NAME': get_secret('DB_NAME'),
        'ATOMIC_REQUESTS': True,
    }
}

SECRET_KEY = get_secret('DEMO_PROJECT_SECRET_KEY'),

INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]

DEBUG = False

# EMAIL_HOST = 'smtp.mandrillapp.com'
# EMAIL_HOST_USER = 'CubaTramites'
# EMAIL_HOST_PASSWORD = 'XSlvFyqDdGF749mvbK45tA'
# EMAIL_PORT = '587'
# EMAIL_USE_TLS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
