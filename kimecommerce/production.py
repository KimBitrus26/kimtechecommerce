from .settings import *

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['kimecommerce.herokuapp.com']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
       "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
# STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
# STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')