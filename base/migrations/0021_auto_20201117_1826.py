# Generated by Django 3.1.3 on 2020-11-17 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_teacher_teachedcourses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='TeachedCourses',
            new_name='CoursesEnrolled',
        ),
    ]