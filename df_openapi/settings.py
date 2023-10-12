from pathlib import Path

from df_api_drf.defaults import (
    DF_API_DRF_INSTALLED_APPS,
    REST_FRAMEWORK,
    SPECTACULAR_SETTINGS,
)
from df_auth.defaults import DF_AUTH_INSTALLED_APPS
from df_remote_config.defaults import DF_REMOTE_CONFIG_INSTALLED_APPS

DEBUG = True

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent

ROOT_URLCONF = "df_openapi.urls"
SECRET_KEY = "111111"
HASHID_FIELD_SALT = "111111"
HASHID_FIELD_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "fcm_django",
    "django_slack",
    "import_export",
    "django_celery_beat",
    "df_notifications",
    "df_chat",
    *DF_API_DRF_INSTALLED_APPS,
    *DF_AUTH_INSTALLED_APPS,
    *DF_REMOTE_CONFIG_INSTALLED_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    "social_core.backends.google.GoogleOAuth2",
]

SITE_ID = 1

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

STATIC_URL = "/static/"
STATIC_ROOT = str(ROOT_DIR / "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = str(ROOT_DIR / "mediafiles")

ALLOWED_HOSTS = ["*"]


DF_NOTIFICATIONS = {
    "CHANNELS": {
        "email": "df_notifications.channels.EmailChannel",
        "console": "df_notifications.channels.ConsoleChannel",
        "push": "df_notifications.channels.FirebasePushChannel",
        "webhook": "df_notifications.channels.JSONPostWebhookChannel",
        "slack": "df_notifications.channels.SlackChannel",
    },
    "SAVE_HISTORY_CONTENT": True,
    "REMINDERS_CHECK_PERIOD": 5,
}


DF_AUTH = {
    "USER_SIGNUP_REQUIRED_FIELDS": {
        "email": "rest_framework.serializers.EmailField",
    },
    "USER_SIGNUP_OPTIONAL_FIELDS": {},
    "USER_SOCIAL_AUTH_FIELDS": {},
    "USER_IDENTITY_FIELDS": {
        "email": "rest_framework.serializers.EmailField",
    },
    "REQUIRED_AUTH_FIELDS": {},
    "OPTIONAL_AUTH_FIELDS": {
        "otp": "rest_framework.serializers.CharField",
    },
    "TEST_USER_EMAIL": None,
    "OTP_IDENTITY_UPDATE_FIELD": True,
    "OTP_DEVICE_MODELS": {
        "email": "django_otp.plugins.otp_email.models.EmailDevice",
        "totp": "django_otp.plugins.otp_totp.models.TOTPDevice",
        "sms": "otp_twilio.models.TwilioSMSDevice",
    },
    "OTP_AUTO_CREATE_ACCOUNT": True,
    "SEND_OTP_UNAUTHORIZED_USER": True,
    "SIGNUP_ALLOWED": True,
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_SCHEMA_CLASS": "df_openapi.schema.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
}

SPECTACULAR_SETTINGS = {
    **SPECTACULAR_SETTINGS,
}
