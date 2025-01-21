# Generated by Django 5.1.5 on 2025-01-20 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_app_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='points_earner',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='screenshots/'),
        ),
    ]
