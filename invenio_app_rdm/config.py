# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
# Copyright (C) 2019 Northwestern University.
#
# Invenio App RDM is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Default configuration for Invenio App RDM.

Each setting has a sensible default value. You overwrite and set
instance-specific configuration by either:

- Configuration file: ``<virtualenv prefix>/var/instance/invenio.cfg``
- Environment variables: ``APP_<variable name>``

"""

from datetime import timedelta


def _(x):
    """Identity function used to trigger string extraction."""
    return x


# Flask
# =====
# See https://flask.palletsprojects.com/en/1.1.x/config/

APP_ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']
"""Allowed hosts.

Since HAProxy and Nginx route all requests no matter the host header
provided, the allowed hosts variable is set to localhost. In production it
should be set to the correct host and it is strongly recommended to only
route correct hosts to the application.
"""

MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100 MiB
"""Max upload size for form data via application/multipart-formdata."""

SECRET_KEY = "CHANGE_ME"
"""Flask secret key.

Each installation (dev, production, ...) needs a separate key.

SECURITY WARNING: keep the secret key used in production secret!
"""

SESSION_COOKIE_SECURE = True
"""Sets cookie with the secure flag by default."""


# Flask-Limiter
# =============
# https://flask-limiter.readthedocs.io/en/stable/#configuration

RATELIMIT_STORAGE_URL = "redis://localhost:6379/3"
"""Storage for ratelimiter."""


# Flask-Babel
# ===========
# See https://pythonhosted.org/Flask-Babel/#configuration

BABEL_DEFAULT_LOCALE = 'en'
"""Default locale (language)."""

BABEL_DEFAULT_TIMEZONE = 'Europe/Zurich'
"""Default time zone."""


# Invenio-I18N
# ============
# See https://invenio-i18n.readthedocs.io/en/latest/configuration.html

# Other supported languages (do not include BABEL_DEFAULT_LOCALE in list).
# I18N_LANGUAGES = [
#     ('fr', _('French'))
# ]


# Invenio-Theme
# =============
# See https://invenio-theme.readthedocs.io/en/latest/configuration.html

BASE_TEMPLATE = 'invenio_app_rdm/page.html'
"""Global base template."""

COVER_TEMPLATE = 'invenio_theme/page_cover.html'
"""Cover page base template (used for e.g. login/sign-up)."""

FOOTER_TEMPLATE = 'invenio_theme/footer.html'
"""Footer base template."""

HEADER_TEMPLATE = 'invenio_theme/header.html'
"""Header base template."""

SETTINGS_TEMPLATE = 'invenio_theme/page_settings.html'
"""Settings base template."""

# Theme configuration
# ===================
#: Site logo
THEME_LOGO = 'images/invenio-rdm.png'
#: Site name
THEME_SITENAME = _('Invenio App RDM')
#: Use default frontpage.
THEME_FRONTPAGE = True
#: Frontpage title.
THEME_FRONTPAGE_TITLE = _('The turn-key research data management repository')
#: Frontpage template.
THEME_FRONTPAGE_TEMPLATE = 'invenio_app_rdm/frontpage.html'
"""Frontpage template."""

THEME_FRONTPAGE_TITLE = _('Invenio App RDM')
"""Frontpage title."""

THEME_LOGO = 'images/invenio-rdm.png'
"""Theme logo."""

THEME_SITENAME = _('InvenioRDM: Turn-key Research Data Management Repository')
"""Site name."""

# Invenio-Mail / Flask-Mail
# =========================
# See https://pythonhosted.org/Flask-Mail/#configuring-flask-mail

MAIL_SUPPRESS_SEND = True
"""Disable email sending by default."""


# Flask-Collect
# =============
# See https://github.com/klen/Flask-Collect#setup

COLLECT_STORAGE = 'flask_collect.storage.file'
"""Static files collection method (defaults to copying files)."""


# Invenio-Accounts
# ================
# (Flask-Security, Flask-Login, Flask-Principal, Flask-KVSession)
# See https://invenio-accounts.readthedocs.io/en/latest/configuration.html
# See https://flask-security.readthedocs.io/en/3.0.0/configuration.html

ACCOUNTS_SESSION_REDIS_URL = 'redis://localhost:6379/1'
"""Redis session storage URL."""

ACCOUNTS_USERINFO_HEADERS = True
"""Enable session/user id request tracing.

This feature will add X-Session-ID and X-User-ID headers to HTTP response. You
MUST ensure that NGINX (or other proxies) removes these headers again before
sending the response to the client. Set to False, in case of doubt.
"""

SECURITY_EMAIL_SENDER = "info@inveniosoftware.org"
"""Email address used as sender of account registration emails."""

SECURITY_EMAIL_SUBJECT_REGISTER = _("Welcome to Invenio App RDM!")
"""Email subject for account registration emails."""


# Invenio-Celery / Celery / Flask-Celeryext
# =========================================
# See https://invenio-celery.readthedocs.io/en/latest/configuration.html
# See docs.celeryproject.org/en/latest/userguide/configuration.html
# See https://flask-celeryext.readthedocs.io/en/latest/

BROKER_URL = "amqp://guest:guest@localhost:5672/"
"""URL of message broker for Celery 3 (default is RabbitMQ)."""

CELERY_BEAT_SCHEDULE = {
    'indexer': {
        'task': 'invenio_indexer.tasks.process_bulk_queue',
        'schedule': timedelta(minutes=5),
    },
    'accounts': {
        'task': 'invenio_accounts.tasks.clean_session_table',
        'schedule': timedelta(minutes=60),
    }
}
"""Scheduled tasks configuration (aka cronjobs)."""

CELERY_BROKER_URL = BROKER_URL
"""Same as BROKER_URL to support Celery 4."""

CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
"""URL of backend for result storage (default is Redis)."""


# Flask-SQLAlchemy
# ================
# See https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://invenio-app-rdm:invenio-app-rdm@localhost/' \
    'invenio-app-rdm'
"""Database URI including user and password.

Default value is provided to make module testing easier.
"""


# Invenio-JSONSchemas
# ===================
# See https://invenio-jsonschemas.readthedocs.io/en/latest/configuration.html

JSONSCHEMAS_HOST = '0.0.0.0'
"""Hostname used in URLs for local JSONSchemas."""


# OAI-PMH
# =======
# See https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py  # noqa
# (Using GitHub because documentation site out-of-sync at time of writing)

OAISERVER_ID_PREFIX = 'oai:invenio-app-rdm.org:'
"""The prefix that will be applied to the generated OAI-PMH ids."""


# Flask-DebugToolbar
# ==================
# See https://flask-debugtoolbar.readthedocs.io/en/latest/#configuration
# Flask-DebugToolbar is by default enabled when the application is running in
# debug mode. More configuration options are available above

DEBUG_TB_INTERCEPT_REDIRECTS = False
"""Switches off incept of redirects by Flask-DebugToolbar."""


# Flask-Caching
# =============
# See https://flask-caching.readthedocs.io/en/latest/index.html#configuring-flask-caching  # noqa

CACHE_REDIS_URL = "redis://localhost:6379/0"
"""URL to connect to Redis server."""

CACHE_TYPE = "redis"
"""Use Redis caching object."""


# Invenio-Search
# ==============
# See https://invenio-search.readthedocs.io/en/latest/configuration.html

SEARCH_ELASTIC_HOSTS = [{"host": "localhost", "port": 9200}]
"""Elasticsearch hosts."""


# Invenio-Base
# ============
# See https://invenio-base.readthedocs.io/en/latest/api.html#invenio_base.wsgi.wsgi_proxyfix  # noqa

WSGI_PROXIES = 2
"""Correct number of proxies in front of your application."""
