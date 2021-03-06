# Generated by Django 2.2.6 on 2020-04-02 22:19

from django.db import migrations, models
import proyectoferreteria.apps.gestionadmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0095_auto_20200402_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Correo_Cliente',
            field=models.EmailField(blank=True, max_length=30, validators=[proyectoferreteria.apps.gestionadmin.models.validarcorreoexistenteCliente]),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='Direccion_Proveedor',
            field=models.TextField(max_length=100, validators=[proyectoferreteria.apps.gestionadmin.models.validardireccion]),
        ),
    ]
