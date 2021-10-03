from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    profile_picture = CloudinaryField('image')

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    media = CloudinaryField('image')
    title = models.CharField(max_length=255)
    caption = models.TextField()
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    # datetime = models.DateTimeField()

    def __str__(self):
        return self.body