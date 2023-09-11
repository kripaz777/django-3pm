# Generated by Django 4.2.4 on 2023-09-11 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_siteinfo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300)),
                ("email", models.EmailField(max_length=200)),
                ("subject", models.TextField()),
                ("message", models.TextField()),
            ],
        ),
    ]