# Generated by Django 4.1 on 2022-10-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0019_remove_league_founded_remove_team_founded"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="footballer",
            name="name",
        ),
        migrations.RemoveField(
            model_name="footballer",
            name="old_club",
        ),
        migrations.AddField(
            model_name="footballer",
            name="player",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Player"
            ),
        ),
        migrations.AddField(
            model_name="footballer",
            name="pos",
            field=models.CharField(
                blank=True, max_length=3, null=True, verbose_name="Pos"
            ),
        ),
        migrations.AlterField(
            model_name="footballer",
            name="age",
            field=models.IntegerField(
                blank=True, max_length=2, null=True, verbose_name="Age"
            ),
        ),
    ]
