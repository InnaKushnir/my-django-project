# Generated by Django 4.1 on 2023-01-30 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0003_dish_cooks"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dish",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="dishtype",
            options={"ordering": ["name"]},
        ),
    ]
