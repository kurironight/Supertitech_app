# Generated by Django 2.1.7 on 2019-09-19 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supertitech', '0023_auto_20190918_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='repu',
            field=models.ForeignKey(on_delete='CASCADE', to='Supertitech.Reputation'),
        ),
    ]