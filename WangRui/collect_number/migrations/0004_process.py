# Generated by Django 4.2.9 on 2024-04-14 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("collect_number", "0003_messagesall_keyword"),
    ]

    operations = [
        migrations.CreateModel(
            name="Process",
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
                ("name", models.CharField(max_length=20)),
                ("keyword", models.CharField(max_length=20)),
                ("hot", models.IntegerField(default=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
