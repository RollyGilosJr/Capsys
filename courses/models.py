from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=250, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # objects = models.Manager()

    def __str__(self):
	    return self.course_name
