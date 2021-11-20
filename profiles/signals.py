from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def user_create_handler(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(user=user,
                                         first_name=user.username,
                                         email=user.email)


@receiver(post_save, sender=Profile)
def profileUpdated(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.username = profile.first_name
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profile)
def profileDeleted(sender, instance, **kwargs):
    user = instance.user
    user.delete()
