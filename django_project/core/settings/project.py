# coding=utf-8

"""Project level settings.

Adjust these values as needed but don't commit passwords etc. to any public
repository!
"""

import os  # noqa
from django.utils.translation import ugettext_lazy as _
from .contrib import *  # noqa

# Project apps
INSTALLED_APPS += (
    'nickle',
)

# Set languages which want to be translated
LANGUAGES = (
    ('en', _('English')),
)

VALID_DOMAIN = [
    '0.0.0.0',
]

PIPELINE = {
    'STYLESHEETS': {
    },
    'JAVASCRIPT': {
    }
}

TEMP_FOLDER = MEDIA_ROOT + '/temp'
