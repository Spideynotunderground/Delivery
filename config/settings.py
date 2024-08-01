"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os.path
from pathlib import Path
from django.utils.translation import gettext

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q$dd3-&ws7c-9q&(ne#kztb=ap*j8fyu8a!23-23@d%ep+)o7z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic'
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'delivery',
    'users',
    'django_browser_reload',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'social_django',
    'django_recaptcha',
    'bigcode',
]

# SOCIAL_AUTH_GOOGLE_CLIENT_ID = '831062076834-7sc66pt8tquu0mhjv9919v85ivu52sa6.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_SECRET = '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'


MIDDLEWARE = [
    "allauth.account.middleware.AccountMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'social_django.context_processors.backends',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.gitlab.GitLabOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

gettext = lambda s: s

LANGUAGES = (
    ('en', gettext('English')),
    ('ru', gettext('Russian')),
)


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'files/static'), ]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'files/uploads')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_GITHUB_KEY = 'Ov23li5EViTbjEzezXMu'
SOCIAL_AUTH_GITHUB_SECRET = 'f09cc5e61af7cbc31f3328cef8d809c02b516654'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

# SOCIAL_AUTH_FACEBOOK_KEY = '789495929694152'
# SOCIAL_AUTH_FACEBOOK_SECRET = 'e4306b845ecd539dad07066085040fa0'
# SOCIAL_AUTH_URL_NAMESPACE = 'social'

# SOCIAL_AUTH_TWITTER_KEY = 'TH0YWavaD0hnsmi8i2VVVJEQQ'
# SOCIAL_AUTH_TWITTER_SECRET = 'iDHSfAk1jyO1yqMpWsVYQGUd20ppMqphNjajYoAeBG471y4tij'
# SOCIAL_AUTH_URL_NAMESPACE = 'social'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'setora087@gmail.com'
# EMAIL_HOST_PASSWORD = 'klbw gfiu dknq fqtr'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


SOCIAL_AUTH_GITLAB_KEY = '13d6eeef2c5570342a5e87e80d1d0b461fcc44026b9ecb1778deac57c517bb7b'
SOCIAL_AUTH_GITLAB_SECRET = 'gloas-4583e72a31510324ec81fa1aa56cf7f296c6b8e21ba000e1039a01bc8e179b83'
SOCIAL_AUTH_GITLAB_SCOPE = ['read_user']
# SOCIAL_AUTH_URL_NAMESPACE = 'social'

# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'setora087@gmail.com'
EMAIL_HOST_PASSWORD = 'bndtuepagzrqncnn'

RECAPTCHA_PUBLIC_KEY = '6LfPdggqAAAAAD0gSRhzV2nE0eRd-P95Ew5kBWv8'
RECAPTCHA_PRIVATE_KEY = '6LfPdggqAAAAAAqnN9iV17p3G9Kg8cauuQTSVMJi'

RECAPTCHA_ERROR_MSG = {
    'required': 'Please complete reCAPTCHA',
}
