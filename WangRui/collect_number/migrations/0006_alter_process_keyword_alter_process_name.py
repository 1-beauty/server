# Generated by Django 4.2.9 on 2024-04-16 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "collect_number",
            "0005_alter_messagesall_hot_alter_messagesall_keyword_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="process", name="keyword", field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="process", name="name", field=models.CharField(max_length=200),
        ),
    ]