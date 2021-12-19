from pathlib import Path

from decouple import config
from easy_thumbnails.conf import Settings as ThumbnailSettings

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config("DJANGO_SECRET_KEY")
DEBUG = config("DJANGO_DEBUG", cast=bool)
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "generic_pages_app.apps.GenericPagesAppConfig",
    "product_viewer_app.apps.ProductViewerAppConfig",
    "ckeditor",
    "easy_thumbnails",
    "image_cropping",
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

ROOT_URLCONF = "django_shop_3.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_shop_3.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DJANGO_DB_NAME"),
        "USER": config("DJANGO_DB_USER"),
        "PASSWORD": config("DJANGO_DB_PASSWORD"),
        "HOST": config("DJANGO_DB_HOST"),
        "PORT": config("DJANGO_DB_PORT"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

CKEDITOR_CONFIGS = {
    # TODO: make custom configs with need to use only options
    "main": {
        "skin": "moono-lisa",
        "toolbar": "Custom",
        "height": 300,
        "toolbar_Custom": [
            ["Styles", "Format"],
            ["Bold", "Italic", "Underline"],
            ["NumberedList", "BulletedList"],
            ["JustifyLeft", "JustifyCenter", "JustifyRight", "JustifyBlock"],
            ["Link", "Unlink"],
            ["Source"],
        ],
    },
}

THUMBNAIL_PROCESSORS = ("image_cropping.thumbnail_processors.crop_corners",) + ThumbnailSettings.THUMBNAIL_PROCESSORS
IMAGE_CROPPING_BACKEND = "image_cropping.backends.easy_thumbs.EasyThumbnailsBackend"
IMAGE_CROPPING_JQUERY_URL = "https://code.jquery.com/jquery-3.6.0.min.js"

LANGUAGE_CODE = "ru-RU"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = (BASE_DIR / "assets",)

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
