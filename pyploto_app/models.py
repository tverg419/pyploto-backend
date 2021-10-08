from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from datetime import datetime
class User(AbstractUser):
    profile_picture = CloudinaryField('image', blank=True)

    def __str__(self):
        return self.username

    def get_full_name(self):
        return super().get_full_name()

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE, related_name='posts', default='')
    media = CloudinaryField('image')
    title = models.CharField(max_length=255)
    caption = models.TextField()
    datetime_modified = models.CharField(max_length=255, blank=False, default=datetime.now().strftime(("%H:%M %m/%d/%y")))

    def __str__(self):
        return self.title

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE, related_name='comments', default='')
    body = models.TextField()
    # datetime = models.DateTimeField()

    def __str__(self):
        return self.body