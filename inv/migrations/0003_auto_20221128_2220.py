# Generated by Django 2.2 on 2022-11-29 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0002_subcategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategoria',
            name='descripcion',
            field=models.CharField(help_text='Descripción de la Categoría', max_length=100),
        ),
    ]