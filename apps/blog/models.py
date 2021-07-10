from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=40, blank=True, null=True)
    img = models.ImageField(upload_to='profile_images', blank=True, null=True)


    def __str__(self):
        return self.nickname

    


@receiver(signals.post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    Profile.objects.create(
        user=instance, 
        nickname=instance.username,
        description=f'My name is -> {instance.username}'
        )

