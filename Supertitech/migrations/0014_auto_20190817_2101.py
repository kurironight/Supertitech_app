# Generated by Django 2.2.1 on 2019-08-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supertitech', '0013_auto_20190817_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrmatrix',
            name='PW',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='qrmatrix',
            name='gakuseki',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
