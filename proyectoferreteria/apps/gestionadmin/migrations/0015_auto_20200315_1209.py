# Generated by Django 2.2.6 on 2020-03-15 18:09

from django.db import migrations, models
import proyectoferreteria.apps.gestionadmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0014_auto_20200313_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correoCliente',
            field=models.EmailField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccionCliente',
            field=models.TextField(validators=[proyectoferreteria.apps.gestionadmin.models.validardireccion]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombreCliente',
            field=models.CharField(max_length=15, validators=[proyectoferreteria.apps.gestionadmin.models.validarnombre]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefonoCliente',
            field=models.CharField(max_length=8, validators=[proyectoferreteria.apps.gestionadmin.models.validarnumero]),
        ),

    ]
