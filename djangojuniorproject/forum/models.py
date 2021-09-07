from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):

    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


# class UserProfile(models.Model):
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     about = models.CharField(max_length=300, blank=True)
#     # avatar = ResizedImageField(size=[230, 230], crop=['middle', 'center'], quality=99, upload_to='profileavatar/%Y/%m/%d', null=True, blank=True)
#
#
# class Comment(models.Model):
#
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comment')
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')


