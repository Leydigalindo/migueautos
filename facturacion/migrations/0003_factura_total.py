# Generated by Django 4.0.2 on 2022-08-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0002_alter_detallefactura_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='total',
            field=models.IntegerField(blank=True, default=0.0),
        ),
    ]