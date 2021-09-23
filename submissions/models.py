from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Submissions(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    duedate = models.DateTimeField()
    sub_details = models.TextField()
    image = models.ImageField(upload_to="images/forum/", default="", blank=True, null=True)

    FileTypeChoices = [
        ('file', 'File'),
        ('text', 'Text'),
        ('url', 'URL')
    ]

    filetype = models.CharField(max_length=10, choices=FileTypeChoices)

    def __str__(self):
        return self.title


class Submit(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    postsub = models.ForeignKey(Submissions, null=True, on_delete=models.CASCADE)
    sub_content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/forum/", default="", blank=True, null=True)

    def __str__(self):
        comment_title = self.user.username + " - " + self.postsub.title
        return comment_title