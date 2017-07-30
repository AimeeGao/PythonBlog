from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(default='')
    author = models.ForeignKey(User,related_name="blog_posts")
    publish = models.DateTimeField(default=timezone.now)



