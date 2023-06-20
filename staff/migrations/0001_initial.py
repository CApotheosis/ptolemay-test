# Generated by Django 4.2.2 on 2023-06-20 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "name",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
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
                ("first_name", models.CharField(max_length=25)),
                ("last_name", models.CharField(max_length=25)),
                ("middle_name", models.CharField(max_length=25)),
                ("position", models.CharField(max_length=30)),
                ("salary", models.IntegerField()),
                ("age", models.IntegerField()),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="staff",
                        to="staff.department",
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["last_name"], name="staff_staff_last_na_d6f35e_idx"
                    )
                ],
            },
        ),
    ]
