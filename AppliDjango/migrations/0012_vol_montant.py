# Generated by Django 4.2.1 on 2023-06-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppliDjango", "0011_remove_reservationchambre_id_facture_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="vol",
            name="montant",
            field=models.IntegerField(default=0),
        ),
    ]