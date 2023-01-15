# Generated by Django 4.1.5 on 2023-01-10 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_deposito_cantidad_deposito_cantidadc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposito',
            name='comida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.comida'),
        ),
        migrations.AlterField(
            model_name='deposito',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.producto'),
        ),
    ]