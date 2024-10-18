from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# import environ
# env = environ.Env()
# environ.Env.read_env()



ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'dbempleado_again',
#         'USER': 'postgres',
#         'PASSWORD': '123456',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
#render postgress data base
import dj_database_url

    #'default':dj_database_url.parse('postgresql://produtiondatabase_user:if6ucxTXfI8sYPXERcKr3doIbKV7CiiX@dpg-cs8jce08fa8c73but0fg-a.ohio-postgres.render.com/produtiondatabase')
DATABASES = {
    # 'default':dj_database_url.parse(env('DATABASE_URL'))
    'default':dj_database_url.parse('postgresql://produtiondatabase_user:if6ucxTXfI8sYPXERcKr3doIbKV7CiiX@dpg-cs8jce08fa8c73but0fg-a/produtiondatabase')

}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'media'
