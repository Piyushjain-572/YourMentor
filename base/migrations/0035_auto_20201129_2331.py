# Generated by Django 3.1.3 on 2020-11-29 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0034_student_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='Type',
            new_name='Designation',
        ),
    ]
