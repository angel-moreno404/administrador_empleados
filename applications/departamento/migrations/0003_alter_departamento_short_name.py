# Generated by Django 4.2.16 on 2024-09-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("departamento", "0002_departamento"),
    ]

    operations = [
        migrations.AlterField(
            model_name="departamento",
            name="short_name",
            field=models.CharField(
                max_length=20, unique=True, verbose_name="Nombre corte"
            ),
        ),
    ]
