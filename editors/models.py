from django.db import models
from blog.models import Post


class Editor(models.Model):
    image = models.ImageField(upload_to="image/")
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    post = models.ManyToManyField(Post, related_name='posts')


    def __str__(self):
        return self.name
