from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class guide(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    pdf = models.FileField(upload_to='guide/', null=True, blank=True)
    image = models.ImageField(upload_to="guide/",null=True, blank=True)

    def __str__(self):
        return self.title



