import os

from configurations import Configuration, values


class Common(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    ENVIRONMENT = values.Value(environ_prefix=None, default='DEVELOPMENT')

    SECRET_KEY = values.SecretValue(environ_prefix=None)

    DEBUG = values.BooleanValue(False)

    TEMPLATE_DEBUG = values.BooleanValue(DEBUG)

    ALLOWED_HOSTS = []

    # Application definition
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',

        # Third Party
        'debug_toolbar',
        'django_extensions',
        'rest_framework',
        'rest_framework_swagger',

        # Apps
        'chatrooms.users',
        'chatrooms.messages',
        'chatrooms.rooms',
    )

    MIDDLEWARE_CLASSES = (
        'djangosecure.middleware.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    # Rest Framework Settings
    REST_FRAMEWORK = {
        'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

        # 'DEFAULT_PERMISSION_CLASSES': (
        #     'rest_framework.permissions.IsAuthenticated',
        # ),
        'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        ),
        'PAGINATE_BY': 25,

        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.UnicodeJSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        )
    }

    # Swagger Rest Framework Doc Settings
    SWAGGER_SETTINGS = {
        "exclude_namespaces": [],
        "api_version": '0.1',
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

    WSGI_APPLICATION = 'chatrooms.wsgi.application'

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
    STATIC_ROOT = 'static'

    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'templates'),
    )

    SITE_ID = 1

    # AUTH_USER_MODEL = 'users.User'


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
