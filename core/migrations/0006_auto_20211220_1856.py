# Generated by Django 3.2.4 on 2021-12-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211220_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esas_sekil', models.ImageField(upload_to='esas sekil')),
            ],
            options={
                'verbose_name': 'Carusel',
                'verbose_name_plural': 'Əsas şəkil',
            },
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Images', 'verbose_name_plural': 'About Approach Şəkil'},
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(default='(+994 12) 570-00-04', max_length=20),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='about_approach_image'),
        ),
    ]