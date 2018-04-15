from django.db.models.signals import post_save, post_delete, post_init
from django.db.models import F
from django.dispatch import receiver
from Comment.models import Comment
from Like.models import Like


@receiver(post_save, sender=Comment)
def save_comment(instance, created=False, **kwargs):
    if created:
        instance.object.__class__.objects.filter(pk=instance.object_id).update(comments_count=F('comments_count') + 1)
        # два похода в базу
        # instance.object.comments_count+=1
        # instance.object.save()


@receiver(post_delete, sender=Comment)
def delete_comment(instance, **kwargs):
    instance.object.__class__.objects.filter(pk=instance.object_id).update(comments_count=F('comments_count') - 1)


@receiver(post_init, sender=Comment)
def watch_is_deleted(instance, **kwargs):
    instance.is_deleted_was = instance.is_deleted


@receiver(post_save, sender=Comment)
def check_is_deleted(instance, **kwargs):
    if instance.is_deleted_was != instance.is_deleted:
        if instance.is_deleted:
            instance.object.__class__.objects.filter(pk=instance.object_id).update(
                comments_count=F('comments_count') - 1)
        else:
            instance.object.__class__.objects.filter(pk=instance.object_id).update(
                comments_count=F('comments_count') + 1)


# def saving_eventable_model(instance,created=False,**kwargs):
#     if created:
#         e=Event()
#         e.title=instance.get_title()
#         e.author-instance.get_author()
#         e.save()
#

@receiver(post_save, sender=Like)
def save_like(instance, created=False, **kwargs):
    if created:
        instance.object.__class__.objects.filter(pk=instance.object_id).update(likes_count=F('likes_count') + 1)


@receiver(post_delete, sender=Like)
def delete_like(instance, **kwargs):
    instance.object.__class__.objects.filter(pk=instance.object_id).update(likes_count=F('likes_count') - 1)


@receiver(post_init, sender=Like)
def watch_like_deleted(instance, **kwargs):
    instance.is_deleted_was = instance.is_deleted


@receiver(post_save, sender=Like)
def check_like_deleted(instance, **kwargs):
    if instance.is_deleted_was != instance.is_deleted:
        if instance.is_deleted:
            instance.object.__class__.objects.filter(pk=instance.object_id).update(
                comments_count=F('likes_count') - 1)
        else:
            instance.object.__class__.objects.filter(pk=instance.object_id).update(
                comments_count=F('likes_count') + 1)
