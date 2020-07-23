# Generated by Django 2.2.6 on 2020-03-06 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0007_cliente_empleado_planilla_turnoempleado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(max_length=15)),
                ('precioVenta', models.IntegerField()),
                ('precioCompra', models.IntegerField()),
                ('existencia', models.IntegerField()),
                ('idCategoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.Categoria')),
                ('idMarca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.Marca')),
            ],
        ),
    ]