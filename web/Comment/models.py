from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from Like.models import LikeMixin
from Main.models import AuthorMixin, DateMixin, TextMixin, DeleteMixin
from django.db import models


class Comment(AuthorMixin, DateMixin, TextMixin, DeleteMixin, LikeMixin):
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object = GenericForeignKey(ct_field='content_type', fk_field='object_id')


class CommentMixin(models.Model):
    comments = GenericRelation(Comment)
    comments_count = models.IntegerField(default=0)

    class Meta:
        abstract = True

