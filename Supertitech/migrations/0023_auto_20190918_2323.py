# Generated by Django 2.1.7 on 2019-09-18 14:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Supertitech', '0022_auto_20190918_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='res',
            name='pinuser',
        ),
        migrations.AddField(
            model_name='res',
            name='pinuser',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
