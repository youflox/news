from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    title       = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    paragraph   = models.TextField(null=False)
    author      = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date        = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(max_length=100, unique=True)
    tags        = models.CharField(max_length=200)
    image       = models.ImageField(upload_to='images', null=False, blank=False)

    def __str__(self):
        return self.title
