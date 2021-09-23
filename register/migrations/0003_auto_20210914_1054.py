# Generated by Django 3.2.7 on 2021-09-14 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_userprofile_group_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='group_id',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='group_name',
            field=models.CharField(default='', max_length=250),
        ),
    ]
