from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_picture = models.ImageField()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    media = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=255)
    caption = models.TextField()
    likes = models.IntegerField()
    datetime = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    datetime = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.body