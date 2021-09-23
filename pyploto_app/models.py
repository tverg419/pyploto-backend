from django.db import models

class Post(models.Model):
    media = models.ImageField()
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    caption = models.TextField()
    likes = models.IntegerField()
    datetime = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    datetime = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.body