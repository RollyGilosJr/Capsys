# Generated by Django 3.2.7 on 2021-09-13 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposalgroup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='group',
            name='user',
        ),
    ]
