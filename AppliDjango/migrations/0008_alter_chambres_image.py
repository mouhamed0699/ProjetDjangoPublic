# Generated by Django 4.2.1 on 2023-05-26 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppliDjango", "0007_alter_chambres_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chambres",
            name="image",
            field=models.CharField(default="", max_length=200),
            preserve_default=False,
        ),
    ]
