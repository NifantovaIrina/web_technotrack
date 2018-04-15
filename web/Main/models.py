from django.db import models

from settings import settings


class DeleteMixin(models.Model):
    is_deleted = models.BooleanField(default=False)

    # def get_formatted_text(self):
    #     return self.text + 'Formatted'

    class Meta:
        abstract = True


class AuthorMixin(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class EventMixin:
    def get_title(self):
        raise NotImplementedError

    def get_author(self):
        raise NotImplementedError


class TextMixin(models.Model):
    text = models.CharField(max_length=255)

    class Meta:
        abstract = True
