import os

from configurations import Configuration, values


class Common(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    ENVIRONMENT = values.Value(environ_prefix=None, default='DEVELOPMENT')

    SECRET_KEY = values.SecretValue(environ_prefix=None)

    DEBUG = values.BooleanValue(False)

    TEMPLATE_DEBUG = values.BooleanValue(DEBUG)

    ALLOWED_HOSTS = ['*', ]

    SESSION_ENGINE = 'redis_sessions.session'
    SESSION_REDIS_PREFIX = 'session'

    # Application definition
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Third Party
        'ws4redis',
        'debug_toolbar',
        'django_extensions',
        'rest_framework',
        'rest_framework_swagger',
        'corsheaders',

        # Apps
        'chatrooms.users',
        'chatrooms.rooms',
        'chatrooms.messages',
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.static',
        'ws4redis.context_processors.default',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    )

    # Rest Framework Settings
    REST_FRAMEWORK = {
        'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

        # 'DEFAULT_PERMISSION_CLASSES': (
        #     'rest_framework.permissions.AllowAny',
        # ),
        'PAGINATE_BY': 25,

        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.UnicodeJSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_FILTER_BACKENDS': (
            'rest_framework.filters.DjangoFilterBackend',
            'rest_framework.filters.SearchFilter',
            'rest_framework.filters.OrderingFilter',
        ),
    }

    # Swagger Rest Framework Doc Settings
    SWAGGER_SETTINGS = {
        "exclude_namespaces": [],
        "api_version": '1.0',
        "api_path": "/",
        "enabled_methods": [
            'get',
            'post',
            'put',
            'patch',
            'delete'
        ],
        "api_key": '',
        "is_authenticated": False,
        "is_superuser": False,
    }

    ROOT_URLCONF = 'chatrooms.urls'

    # Database
    # https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = values.DatabaseURLValue(
        'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3')))

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/
    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.6/howto/static-files/

    STATIC_ROOT = 'staticfiles'

    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'templates'),
    )

    AUTH_USER_MODEL = 'users.User'

    WSGI_APPLICATION = 'ws4redis.django_runserver.application'

    WEBSOCKET_URL = '/ws/'
    WS4REDIS_EXPIRE = 7200

    WS4REDIS_HEARTBEAT = '--heartbeat--'
    WS4REDIS_HOST = values.Value(environ_prefix=None, default='localhost')
    WS4REDIS_PORT = values.IntegerValue(environ_prefix=None, default=6379)
    WS4REDIS_CONNECTION = {
        'host': WS4REDIS_HOST,
        'port': WS4REDIS_PORT,
    }

    # CORS settings
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_URLS_REGEX = r'^/api-v1/.*$'
    CORS_ALLOW_METHODS = (
        'GET',
        'POST',
        'PUT',
        'PATCH',
        'DELETE',
        'OPTIONS'
    )
    CORS_ALLOW_HEADERS = (
        'x-requested-with',
        'content-type',
        'accept',
        'origin',
        'authorization',
        'x-csrftoken'
    )
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "console": {
                "level": "INFO",
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
            }
        }
    }


class Development(Common):
    DEBUG = True

    TEMPLATE_DEBUG = DEBUG

    PROTOCOL = 'http'

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # Dummy cache for development
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }


class Production(Common):
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
