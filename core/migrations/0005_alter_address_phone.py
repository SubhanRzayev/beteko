# Generated by Django 3.2.4 on 2021-11-03 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_address_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.IntegerField(default='012-574-00-04'),
        ),
    ]