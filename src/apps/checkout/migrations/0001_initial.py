# Generated by Django 3.1.6 on 2021-02-09 15:04

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactOptions",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("whatsapp", models.BooleanField()),
                ("messenger", models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file_name", models.CharField(max_length=30)),
                ("alt", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Portfolio",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file_name", models.CharField(max_length=30)),
                ("alt", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="ProfessionOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("profession", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("image", models.CharField(max_length=30)),
                ("quote", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="PageOptions",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "custom_portfolio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="checkout.portfolio",
                    ),
                ),
                (
                    "custom_reviews",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="checkout.review",
                    ),
                ),
                (
                    "professions",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="checkout.professionoption",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CheckoutOptions",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                (
                    "contact_options",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="checkout.contactoptions",
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="checkout.image",
                    ),
                ),
                (
                    "page_options",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="checkout.pageoptions",
                    ),
                ),
            ],
        ),
    ]
