# Generated by Django 3.1.3 on 2020-11-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_auto_20201119_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
