# Generated by Django 3.2.4 on 2021-12-20 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pdfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfile',
            name='careers',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='careers_required', to='core.careers'),
        ),
    ]