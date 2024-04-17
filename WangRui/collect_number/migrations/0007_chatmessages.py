# Generated by Django 4.2.9 on 2024-04-16 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("collect_number", "0006_alter_process_keyword_alter_process_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatMessages",
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
                ("text", models.CharField(max_length=400)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]