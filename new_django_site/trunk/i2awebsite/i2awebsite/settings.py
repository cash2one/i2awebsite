"""
Django settings for i2awebsite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import platform
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm2jqmdqd3#cx3=9$f91td^tulvz$-1+fip_%s61dq+=)23qegj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1',
                 'i2asolutions.com',
                 'www.i2asolutions.com']

ADMINS = MANAGERS = (
    ('Mariusz Okulanis', 'mokulanis@i2asolutions.com'),
    ('Pawel Roman', 'proman@i2asolutions.com'),
)

EMAIL_HOST = 'xmail.i2asolutions.com'
EMAIL_HOST_USER = 'mailer@qa.i2asolutions.com'
EMAIL_HOST_PASSWORD = 'Dakawadjoks4'
EMAIL_SUBJECT_PREFIX = '[I2A Website]'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'I2A Website <noreply@qa.i2asolutions.com>'
SERVER_EMAIL = 'I2A Website <noreply@qa.i2asolutions.com>'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'i2awebsite.urls'

WSGI_APPLICATION = 'i2awebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/static/'

# import machine-specific settings
try:
    execfile('%s/i2awebsite/local-settings/%s.py' % (BASE_DIR.replace('\\','/'),
        'settings-%s' % platform.node().replace('.', '_')))
except:
    print "Local settings file not found"