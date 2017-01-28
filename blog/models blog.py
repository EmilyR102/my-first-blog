from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	titl = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	