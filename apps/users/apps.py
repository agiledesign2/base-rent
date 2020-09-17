from django.apps import AppConfig
from django.conf import settings

from imagekit import register

from .utils import load_path_attr


class UsersAppConfig(AppConfig):

    name = "users"
    verbose_name = "users"

    def ready(self):
        thumbnail_path = getattr(
            settings,
            "USERS_IMAGES_THUMBNAIL_SPEC",
            "users.specs.ImageThumbnail"
        )
        thumbnail_spec_class = load_path_attr(thumbnail_path)
        register.generator("users:avatar:thumbnail", thumbnail_spec_class)

        list_thumbnail_path = getattr(
            settings,
            "USERS_IMAGES_LIST_THUMBNAIL_SPEC",
            "users.specs.ImageListThumbnail"
        )
        list_thumbnail_spec_class = load_path_attr(list_thumbnail_path)
        register.generator("users:avatar:list_thumbnail", list_thumbnail_spec_class)

        small_thumbnail_path = getattr(
            settings,
            "USERS_IMAGES_SMALL_THUMBNAIL_SPEC",
            "users.specs.ImageSmallThumbnail"
        )
        small_thumbnail_spec_class = load_path_attr(small_thumbnail_path)
        register.generator("users:avatar:small_thumbnail", small_thumbnail_spec_class)

        medium_thumbnail_path = getattr(
            settings,
            "USERS_IMAGES_MEDIUM_THUMBNAIL_SPEC",
            "users.specs.ImageMediumThumbnail"
        )
        medium_thumbnail_spec_class = load_path_attr(medium_thumbnail_path)
        register.generator("users:avatar:medium_thumbnail", medium_thumbnail_spec_class)

        try:
            pass
            #import users.signals  # noqa F401
        except ImportError:
            pass
