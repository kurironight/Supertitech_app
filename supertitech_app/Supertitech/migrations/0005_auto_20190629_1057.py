# Generated by Django 2.1.7 on 2019-06-29 01:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supertitech', '0004_profilimage_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilimage',
            name='owner',
            field=models.OneToOneField(default=1, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]