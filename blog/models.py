from django.db import models

from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True) 
    summary = models.TextField(max_length=500)
    content = models.TextField()

    def __str__(self):
        return self.title
