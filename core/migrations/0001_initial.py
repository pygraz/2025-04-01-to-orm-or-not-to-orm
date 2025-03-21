# Copyright (c) 2025 Python User Group Graz. Distributed under the MIT license.
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Label",
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
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Issue",
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
                ("title", models.CharField(max_length=100)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("todo", "Todo"),
                            ("doing", "Doing"),
                            ("done", "Done"),
                        ],
                        default="todo",
                    ),
                ),
                ("description", models.TextField(max_length=2000)),
                (
                    "assignee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issues",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "labels",
                    models.ManyToManyField(related_name="issues", to="core.label"),
                ),
            ],
        ),
    ]
