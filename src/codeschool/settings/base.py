"""
Django settings for codeschool project. Unlsess you know what you are doing,
installation-specific settings should be configured in the file
settings/codeschool.py

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from codeschool.settings.codeschool import *
from codeschool.settings.template_map import FORCE_JINJA_TEMPLATES

# ./codeschool/src/codeschool
CODESCHOOL_APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ./codeschool/src/
SOURCE_FOLDER_DIR = os.path.dirname(CODESCHOOL_APP_DIR)

# ./codeschool
PROJECT_DIR = os.path.dirname(SOURCE_FOLDER_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    # Local apps
    'cs_core',
    'cs_pages',
    'cs_search',
    'cs_auth',
    'cs_courses',
    'cs_questions',
    'cs_activities',
    'viewpack',
    'srvice',

    # Wagtail and dependencies
    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',
    'modelcluster',
    'compressor',
    'taggit',

    # 3rd party
    #'debug_toolbar',
    'address',
    'annoying',
    'djangobower',
    'djinga',
    'django_extensions',
    'easy_thumbnails',
    'guardian',
    'rest_framework',
    'userena',

    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
] + CODESCHOOL_PLUGINS

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
]


# Authentication backends

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)
ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE = 'cs_auth.Profile'


# Userena support

USERENA_SIGNIN_REDIRECT_URL = '/accounts/%(username)s/'
USERENA_ACTIVATION_REQUIRED = False
USERENA_SIGNIN_AFTER_SIGNUP = True
USERENA_DISABLE_PROFILE_LIST = True
USERENA_ACTIVATION_DAYS = 7
USERENA_FORBIDDEN_USERNAMES = (
    'signup', 'signout', 'signin', 'activate', 'me', 'password', 'login',
    'codeschool')
USERENA_USE_HTTPS = False
USERENA_REGISTER_PROFILE = False

LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
SITE_ID = 1

# Email support

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'


# Gmail support

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'yourgmailaccount@gmail.com'
EMAIL_HOST_PASSWORD = 'yourgmailpassword'


# URLs configuration

ROOT_URLCONF = 'codeschool.urls'


# Templates
# we have to import filters explicitly until a bug is fixed in djinga.

from codeschool.jinja.filters import markdown, icon
from codeschool.jinja.globals import template_vars
from codeschool.jinja.compat import django_compat_finalizer
import codeschool.jinja.ext

TEMPLATES = [
    {
        'BACKEND': 'djinga.backends.djinga.DjingaTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(CODESCHOOL_APP_DIR, 'templates'),
        ],
        'OPTIONS': {
            # These have no effects since we are overloading "condition"
            "jj_exts": ('jinja2', 'jinja'),
            "dj_exts": ('html', 'htm'),
            #"load_from": ("codeschool.filters",),  # wait until djinga fixes problems with python 3
            "i18n_new_style": True,
            "condition": lambda x: (
                x.endswith('.jinja2') or x.endswith('jinja') or
                x in FORCE_JINJA_TEMPLATES),
            "trim_blocks": True,
            "lstrip_blocks": True,
            "finalize": django_compat_finalizer,
            'extensions': [
                'codeschool.jinja.ext.DjangoComment',
                'codeschool.jinja.ext.DjangoLoad',
                'compressor.contrib.jinja2ext.CompressorExtension',
                'wagtail.wagtailcore.jinja2tags.core',
                'wagtail.wagtailadmin.jinja2tags.userbar',
                'wagtail.wagtailimages.jinja2tags.images',
                'jdj_tags.extensions.DjangoL10n',
                #'jdj_tags.extensions.DjangoNow',  # not released yet!
                'djinga.ext.static',
                'djinga.ext.css',
                'djinga.ext.js',
                'djinga.ext.media',
                'djinga.ext.django',
                'djinga.ext.csrf_token',
                'djinga.ext.url',
                #'djinga.ext.htmlcompress.HTMLCompress',  # only on deploy
                "jinja2.ext.do",
                "jinja2.ext.loopcontrols",
                "jinja2.ext.with_",
                "jinja2.ext.i18n",
                "jinja2.ext.autoescape",
            ],
            "context_processors": [
                'django.template.context_processors.request',
                "django.contrib.auth.context_processors.auth",
                #"django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
            "filters": {
                'markdown': markdown,
                'icon': icon,
            },
            'globals': {
                'template_vars': template_vars,
            },
        },
    },
]


WSGI_APPLICATION = 'codeschool.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SOURCE_FOLDER_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'America/Sao_Paulo'  # or 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    'djangobower.finders.BowerFinder',
]

STATICFILES_DIRS = [
    os.path.join(CODESCHOOL_APP_DIR, 'static'),
    os.path.join(CODESCHOOL_APP_DIR, 'bower'),
]

STATIC_ROOT = os.path.join(PROJECT_DIR, 'collect', 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'collect', 'media')
MEDIA_URL = '/media/'

# Enable django compressor
COMPRESS_ENABLED = True
#COMPRESS_JINJA2_GET_ENVIRONMENT = None
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.rCSSMinFilter',
    #'compressor.filters.cssmin.CSSCompressorFilter',
]
COMPRESS_PRECOMPILERS = [
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
    ('text/stylus', 'stylus < {infile} > {outfile}'),
]


# Bower applications

BOWER_COMPONENTS_ROOT = os.path.join(CODESCHOOL_APP_DIR, 'bower/')
BOWER_INSTALLED_APPS = [
    'jquery',
    # 'modernizr',
    'mustache',
    'normalize.css',
    'codemirror',
    'highlight',
    'ace-builds',
    'material-design-lite',
    'dialog-polyfill',

    # Styling
    #'font-roboto#^1.0.1',

    # All polymer dependencies
    'Polymer/polymer',
    'PolymerElements/gold-cc-cvc-input',
    'PolymerElements/gold-cc-expiration-input',
    'PolymerElements/gold-cc-input',
    'PolymerElements/gold-email-input',
    'PolymerElements/gold-phone-input',
    'PolymerElements/gold-zip-input',
    'PolymerElements/iron-a11y-announcer',
    'PolymerElements/iron-a11y-keys',
    'PolymerElements/iron-a11y-keys-behavior',
    'PolymerElements/iron-ajax',
    'PolymerElements/iron-autogrow-textarea',
    'PolymerElements/iron-behaviors',
    'PolymerElements/iron-checked-element-behavior',
    'PolymerElements/iron-collapse',
    'PolymerElements/iron-component-page',
    'PolymerElements/iron-doc-viewer',
    'PolymerElements/iron-dropdown',
    'PolymerElements/iron-elements',
    'PolymerElements/iron-fit-behavior',
    'PolymerElements/iron-flex-layout',
    'PolymerElements/iron-form',
    'PolymerElements/iron-form-element-behavior',
    'PolymerElements/iron-icon',
    'PolymerElements/iron-icons',
    'PolymerElements/iron-iconset',
    'PolymerElements/iron-iconset-svg',
    'PolymerElements/iron-image',
    'PolymerElements/iron-input',
    'PolymerElements/iron-jsonp-library',
    'PolymerElements/iron-list',
    'PolymerElements/iron-localstorage',
    'PolymerElements/iron-media-query',
    'PolymerElements/iron-menu-behavior',
    'PolymerElements/iron-meta',
    'PolymerElements/iron-overlay-behavior',
    'PolymerElements/iron-pages',
    'PolymerElements/iron-range-behavior',
    'PolymerElements/iron-resizable-behavior',
    'PolymerElements/iron-selector',
    'PolymerElements/iron-signals',
    'PolymerElements/iron-test-helpers',
    'PolymerElements/iron-validatable-behavior',
    'PolymerElements/iron-validator-behavior',
    'PolymerElements/neon-animation',
    'PolymerElements/neon-elements',
    'PolymerElements/paper-badge',
    'PolymerElements/paper-behaviors',
    'PolymerElements/paper-button',
    'PolymerElements/paper-card',
    'PolymerElements/paper-checkbox',
    'PolymerElements/paper-dialog',
    'PolymerElements/paper-dialog-behavior',
    'PolymerElements/paper-dialog-scrollable',
    'PolymerElements/paper-drawer-panel',
    'PolymerElements/paper-dropdown-menu',
    'PolymerElements/paper-elements',
    'PolymerElements/paper-fab',
    'PolymerElements/paper-header-panel',
    'PolymerElements/paper-icon-button',
    'PolymerElements/paper-input',
    'PolymerElements/paper-item',
    'PolymerElements/paper-listbox',
    'PolymerElements/paper-material',
    'PolymerElements/paper-menu',
    'PolymerElements/paper-menu-button',
    'PolymerElements/paper-progress',
    'PolymerElements/paper-radio-button',
    'PolymerElements/paper-radio-group',
    'PolymerElements/paper-ripple',
    'PolymerElements/paper-scroll-header-panel',
    'PolymerElements/paper-slider',
    'PolymerElements/paper-spinner',
    'PolymerElements/paper-styles',
    'PolymerElements/paper-tabs',
    'PolymerElements/paper-toast',
    'PolymerElements/paper-toggle-button',
    'PolymerElements/paper-toolbar',
    'PolymerElements/paper-tooltip',
    'PolymerElements/platinum-bluetooth',
    'PolymerElements/platinum-elements',
    'PolymerElements/platinum-https-redirect',
    'PolymerElements/platinum-push-messaging',
    'PolymerElements/platinum-sw',

    # 3rd party web components
    'Sortable',
]


# Django REST framework settings

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


# Wagtail settings

WAGTAIL_SITE_NAME = "codeschool"

