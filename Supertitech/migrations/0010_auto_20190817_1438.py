# Generated by Django 2.2.1 on 2019-08-17 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supertitech', '0009_auto_20190817_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrmatrix',
            name='B1',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='qrmatrix',
            name='B2',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='qrmatrix',
            name='B4',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='qrmatrix',
            name='A3',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='qrmatrix',
            name='A4',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
