# Generated by Django 4.2.3 on 2023-07-27 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="description",
            field=models.TextField(max_length=200),
        ),
    ]
