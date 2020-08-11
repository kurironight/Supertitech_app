# Generated by Django 2.1.7 on 2019-06-29 01:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Supertitech', '0003_profilimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilimage',
            name='owner',
            field=models.ForeignKey(default=1, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]
