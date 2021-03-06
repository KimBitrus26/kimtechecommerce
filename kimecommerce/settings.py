import os
from decouple import config
import dj_database_url 
from whitenoise import WhiteNoise

ENVIRONMENT = os.getenv('ENVIRONMENT', 'production')

DEBUG = False #True
#DEBUG = config('DEBUG', default=False, cast=bool)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '-05sgp9!deq=q1nltm@^^2cc+v29i(tyybv3v2t77qi66czazj'
#SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = ['kimecommerce.herokuapp.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'core',
    'crispy_forms',
    'django_countries',
    'squareconnect',
    'whitenoise',
    'gunicorn',

    'psycopg2'
    
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'kimecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_files')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' #whitenoise.django.GzipManifestStaticFilesStorage'
DBUS_CFLAGS= False
DBUS_LIBS =False

DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.sqlite3",
        # "NAME": os.path.join(BASE_DIR, 'db.sqlite3')
        
    }
}

if ENVIRONMENT == 'production':
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


#Authentication
AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 1

LOGIN_REDIRECT_URL = "/"

CRISPY_TEMPLATE_PACK = "bootstrap4"

STRIPE_PUBLIC_KEY = 'pk_test_51IQVmdBnuvfAc1PJVBLJu0JBrO7ZxJ03ensUSK6T5av6SDrOyVsZNSHR9RgbAxfhEnD46BYvgQGoqpA5YOxpqX0D00YTURh4qZ'

#STRIPE_SECRET_KEY = 'sk_test_51IQVmdBnuvfAc1PJJX3QZT6H3J5NE5N9n6KI4CrWvuYDBInpQo4jspP9RCXWACV336QBPygChFhJok5f7d8MNeUw002uT40MWE'
STRIPE_SECRET_KEY = 'sk_test_51IQVmdBnuvfAc1PJJX3QZT6H3J5NE5N9n6KI4CrWvuYDBInpQo4jspP9RCXWACV336QBPygChFhJok5f7d8MNeUw002uT40MWE'

prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)