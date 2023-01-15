# Generated by Django 4.1.5 on 2023-01-12 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_venta_can1_venta_can2_venta_can3_venta_can4_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='can1',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='can2',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='can3',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='can4',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='can5',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='can6',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='can7',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='can8',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='pro1',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='pro2',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='pro3',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='pro4',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='pro5',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='pro6',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='pro7',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='pro8',
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('subtotal', models.IntegerField(blank=True, null=True)),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.venta')),
            ],
        ),
    ]
