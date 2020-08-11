# Generated by Django 2.1.7 on 2019-09-18 06:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Supertitech', '0021_subject_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='res',
            name='pinuser',
            field=models.ForeignKey(default=1, on_delete='CASCADE', related_name='PinToRes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='res',
            name='owner',
            field=models.ForeignKey(on_delete='CASCADE', related_name='Res', to=settings.AUTH_USER_MODEL),
        ),
    ]