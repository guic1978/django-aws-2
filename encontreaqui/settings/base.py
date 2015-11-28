"""
Django settings for encontreaqui project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import emailcredencials

ADMINS = (
    ('Guilherme Reis', 'guilherme.guic@gmail.com'),
)

MANAGERS = ADMINS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

#Django Registration
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/'
SITE_ID = 1

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e(ggkf(0^)*rvb@ab-#hqq_!+m^+#wr8il@g2!dx&5s_n#0b1('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATE_FORMAT = '%d-%m-%Y'
SHORT_DATETIME_FORMAT = DATE_FORMAT
TIME_FORMAT = '%H:%M'
DATETIME_FORMAT = DATE_FORMAT + ' ' + TIME_FORMAT

# Application definition
INSTALLED_APPS = (
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # EXTERNO
    'mptt',
    'django_mptt_admin',
    'registration',
    'widget_tweaks',
    'imagekit',
    'tinymce',
    # INTERNO
    'core',
    'produtos',
    # 'pedidos',
    'perfis',
    # 'contato',
    'carrinho',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'encontreaqui.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.static',
                'carrinho.context_processors.checa_carrinho',
                'produtos.context_processors.get_categorias_menu',
            ],
        },
    },
]

WSGI_APPLICATION = 'encontreaqui.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, "core/media")
STATIC_ROOT = os.path.join(BASE_DIR, "core/static")
UPLOADS_PROTEGIDOS = os.path.join(BASE_DIR, "core/protegido")

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TINYMCE_JS_URL = os.path.join(STATIC_URL, "tiny_mce/tiny_mce.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_URL, "tiny_mce")
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}

EMAIL_HOST          = 'smtp.sendgrid.net'
EMAIL_PORT          = 587
EMAIL_HOST_USER     = emailcredencials.EMAIL_USER
EMAIL_HOST_PASSWORD = emailcredencials.EMAIL_PASSWORD
EMAIL_USE_TLS       = True
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_HOST          = 'smtp.zoho.com'
# EMAIL_PORT          = 587
# EMAIL_HOST_USER     = 'guilhermereis@bussolatech.com.br'
# EMAIL_HOST_PASSWORD = 'zoho1234@'
# EMAIL_USE_TLS       = True
# EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'

