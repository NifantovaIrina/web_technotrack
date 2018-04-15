from django.apps import AppConfig


class PostConfig(AppConfig):
    name = 'Post'

    def ready(self):
        from . import signals