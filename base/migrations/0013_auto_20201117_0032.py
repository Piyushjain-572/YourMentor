# Generated by Django 3.1.3 on 2020-11-16 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20201116_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Courses_enrolled',
            new_name='Coursesenrolled',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='Courses_enrolled',
            new_name='Coursesenrolled',
        ),
    ]