# Generated by Django 2.1.7 on 2019-09-15 01:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supertitech', '0019_auto_20190915_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastexamfile',
            name='owner',
            field=models.ForeignKey(default=1, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]