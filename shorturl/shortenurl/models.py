from django.db import models

# Create your models here.


class URL(models.Model):
    tiny_url = models.SlugField(max_length=6,primary_key=True)
    original_url = models.URLField(max_length=200, null =False, blank=False)
    created_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    expired_at = models.CharField(null=False, blank=False, max_length=20)
