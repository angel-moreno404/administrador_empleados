# Generated by Django 4.2.16 on 2024-09-25 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("persona", "0003_persona_hoja_vida"),
    ]

    operations = [
        migrations.RenameField(
            model_name="persona", old_name="Departamento", new_name="departamento",
        ),
    ]
