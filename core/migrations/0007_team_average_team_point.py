# Generated by Django 4.1 on 2022-09-05 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_remove_team_average_remove_team_point"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="average",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="team",
            name="point",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
