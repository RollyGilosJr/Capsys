# Generated by Django 3.2.7 on 2021-09-21 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20210914_1054'),
        ('subjects', '0006_remove_subject_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='cp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.userprofile'),
        ),
    ]
