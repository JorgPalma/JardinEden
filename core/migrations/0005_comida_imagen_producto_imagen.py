# Generated by Django 4.1.5 on 2023-01-10 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_cantidad_detalleventa_cantidadc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comida',
            name='imagen',
            field=models.ImageField(null=True, upload_to='comidas'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]