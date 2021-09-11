from django.db import models
from django.contrib.auth import get_user_model

from django_resized import ResizedImageField

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile',
    )

    avatar = ResizedImageField(size=[230, 230], crop=['middle', 'center'], quality=99, upload_to='profile/%Y/%m/%d',
                               blank=True, default='profile/default/default.apng')
    about = models.TextField(default='', blank=True)

    subscribers = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.user} - {self.user.pk}'
