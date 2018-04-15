from django.contrib import admin
from Like.models import Like
from Post.models import Post
from Comment.models import Comment
from User.models import User

admin.site.register(User)
admin.site.register(Like)
admin.site.register(Post)
admin.site.register(Comment)