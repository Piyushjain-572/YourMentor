# Generated by Django 3.1.3 on 2020-11-17 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_auto_20201117_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='TeachedCourses',
        ),
    ]
