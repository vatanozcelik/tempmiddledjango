# Generated by Django 4.1 on 2022-10-06 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0024_alter_footballer_position"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="footballer",
            options={"ordering": ("position",)},
        ),
    ]
