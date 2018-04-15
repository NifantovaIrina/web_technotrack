from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from Main.models import AuthorMixin, DeleteMixin
from django.db import models


class Like(AuthorMixin, DeleteMixin):
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object = GenericForeignKey(ct_field='content_type', fk_field='object_id')

    class Meta:
        unique_together = ('author', 'object_id', 'content_type')


class LikeMixin(models.Model):
    likes = GenericRelation(Like)
    likes_count = models.IntegerField(default=0)

    class Meta:
        abstract = True
