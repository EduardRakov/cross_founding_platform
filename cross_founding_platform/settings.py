# Django settings for cross_founding_platform project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

#PASSWORD_HASHERS = (
#    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
#    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
#    'django.contrib.auth.hashers.BCryptPasswordHasher',
#    'django.contrib.auth.hashers.SHA1PasswordHasher',
#    'django.contrib.auth.hashers.MD5PasswordHasher',
#    'django.contrib.auth.hashers.CryptPasswordHasher',
##    'root',
#    )


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cfpdb',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'root',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/Kiev'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


MEDIA_ROOT = '/home/dmitryg/PycharmProjects/cross_founding_platform/templates'

MEDIA_URL = '/media/'

STATIC_ROOT = '/home/dmitryg/PycharmProjects/cross_founding_platform/cross_founding_platform/cross_founding/templates/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    '/home/dmitryg/PycharmProjects/cross_founding_platform/templates',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'gs-lxj*lkl1qvkcgz+ao(hyyp&amp;&amp;0@l2qhep0sni%t!b(_0k2jk'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
    )

LOGIN_REDIRECT_URL = '/accounts/profile'

SESSION_EXPIRE_AT_BROWSER_CLOSE = False

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

ROOT_URLCONF = 'cross_founding_platform.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'cross_founding_platform.wsgi.application'

TEMPLATE_DIRS = ('/home/dmitryg/PycharmProjects/cross_founding_platform/templates',)
#
#TEMPLATE_CONTEXT_PROCESSORS = (
#    "django.core.context_processors.request",
#    "allauth.account.context_processors.account",
#    "allauth.socialaccount.context_processors.socialaccount",
#    )

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",

    )

AUTH_USER_EMAIL_UNIQUE = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False

#BANDIT_EMAIL = 'bandit@example.com'
DEFAULT_FROM_EMAIL = 'info@google.ru'
#EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'  #email in file
#EMAIL_FILE_PATH = '/home/dmitryg/test_email_folder/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #email in console
#EMAIL_BACKEND = 'bandit.backends.smtp.HijackSMTPBackend' #bandit email

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',
    'registration',
    'django_nose',
    'cross_founding_platform.cross_founding.templatetags',
    'bandit',
    'selenium',
    'splinter',
#    'allauth',
#    'allauth.account',
#    'allauth.socialaccount',
#    'allauth.socialaccount.providers.facebook',
    'cross_founding_platform.cross_founding',
    )

SOCIALACCOUNT_PROVIDERS =\
{ 'facebook':
      { 'SCOPE': ['email', 'publish_stream'],
        'METHOD': 'oauth2' ,
        'LOCALE_FUNC': 'path.to.callable'} }

AUTH_PROFILE_MODULE = 'cross_founding.model.backer'

ACCOUNT_ACTIVATION_DAYS = 2

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
