# Generated by Django 2.1.7 on 2019-08-25 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supertitech', '0014_auto_20190817_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='testdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data1', models.TextField(max_length=100)),
                ('data2', models.TextField(max_length=100)),
                ('data3', models.TextField(max_length=100)),
                ('data4', models.TextField(max_length=100)),
                ('data5', models.TextField(max_length=100)),
                ('data6', models.TextField(max_length=100)),
            ],
        ),
    ]