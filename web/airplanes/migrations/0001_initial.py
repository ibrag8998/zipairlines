# Generated by Django 4.1 on 2022-09-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Airplane",
            fields=[
                (
                    "id",
                    models.PositiveIntegerField(
                        primary_key=True, serialize=False, verbose_name="id"
                    ),
                ),
                (
                    "passengers",
                    models.PositiveIntegerField(verbose_name="passengers amount"),
                ),
            ],
            options={
                "verbose_name": "airplane",
                "verbose_name_plural": "airplanes",
            },
        ),
    ]
