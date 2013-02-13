# Django settings for cross_founding_platform project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cfpdb', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'root', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/Kiev'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


MEDIA_ROOT = '/home/eduardr/PycharmProjects/cross_founding_platform/templates'
MEDIA_URL = '/media/'

STATIC_ROOT = '/home/eduardr/PycharmProjects/cross_founding_platform/cross_founding_platform/cross_founding/static_collected'
STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/accounts/profile'
LOGIN_URL = '/accounts/login'

STATICFILES_DIRS = (
    '/home/eduardr/PycharmProjects/cross_founding_platform/templates',
    )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'gs-lxj*lkl1qvkcgz+ao(hyyp&amp;&amp;0@l2qhep0sni%t!b(_0k2jk'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
    )

SESSION_COOKIE_AGE = 7200
#SESSION_EXPIRE_AT_BROWSER_CLOSE = True

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#    'auth_remember.middleware.AuthRememberMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

ROOT_URLCONF = 'cross_founding_platform.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'cross_founding_platform.wsgi.application'

TEMPLATE_DIRS = ('/home/eduardr/PycharmProjects/cross_founding_platform/templates',)

AUTHENTICATION_BACKENDS = (
    'cross_founding_platform.cross_founding.backends.ThirdPartyAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
    )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    #'django.contrib.admindocs',
    #'south',
    'oauth2',
    'registration',
    'django_nose',
    'cross_founding_platform.cross_founding',
)

AUTH_USER_EMAIL_UNIQUE = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'info@example.com'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

FACEBOOK_OAUTH_DIALOG_URL = "https://www.facebook.com/dialog/oauth?"
FACEBOOK_ACCESS_TOKEN_URL = 'https://graph.facebook.com/oauth/access_token?'
FACEBOOK_GRAPH_API_URL = 'https://graph.facebook.com/me?access_token='
FACEBOOK_REDIRECT_URI = 'http://127.0.0.1:8000/facebook_register/'
FACEBOOK_APP_ID = '467506353311178'
FACEBOOK_APP_SECRET = 'd5f87532dc5623a3373453c61ba3f0c9'

TWITTER_REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
TWITTER_ACCESS_TOKEN_URL  = 'https://api.twitter.com/oauth/access_token'
TWITTER_AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
TWITTER_AUTHENTICATE_URL = 'https://api.twitter.com/oauth/authenticate?oauth_token='
TWITTER_OAUTH_CONSUMER_KEY = "SiAxtvUQc6Z6bVR2Vi0A"
TWITTER_OAUTH_CONSUMER_SECRET_KEY = "sQgtyyO7siQyqEx6609ZfC052lOzsmGSOOh9VG0yvuk"

AUTH_PROFILE_MODULE = 'cross_founding.Backer'

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