# Generated by Django 2.1.7 on 2019-09-10 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Supertitech', '0017_auto_20190910_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentfile',
            name='year',
        ),
        migrations.RemoveField(
            model_name='pastexamfile',
            name='year',
        ),
    ]
