from Comment.models import CommentMixin
from Like.models import LikeMixin
from Main.models import AuthorMixin, DateMixin, TextMixin, DeleteMixin
from django.db import models


class Post(AuthorMixin, DateMixin, TextMixin, DeleteMixin, CommentMixin, LikeMixin):
    title = models.CharField(max_length=255)


