# coding=utf-8
"""
core.settings.contrib
"""
from .base import *  # noqa
import os


STOP_WORDS = (
    'a', 'an', 'and', 'if', 'is', 'the', 'in', 'i', 'you', 'other',
    'this', 'that', 'to',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS += (
    'pipeline.finders.PipelineFinder',
)

# Django-allauth related settings
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Grapelli settings
GRAPPELLI_ADMIN_TITLE = 'Dime Tracker Admin Page'

INSTALLED_APPS += (
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'rest_framework',
    'pipeline',
)

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': ['user:email', 'public_repo', 'read:org']
    }
}

ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_SIGNUP_FORM_CLASS = 'base.forms.SignupForm'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
LOGIN_REDIRECT_URL = "/"
