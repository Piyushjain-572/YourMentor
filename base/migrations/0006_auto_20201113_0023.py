# Generated by Django 3.1.3 on 2020-11-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_course_coordinator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
