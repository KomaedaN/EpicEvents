# Generated by Django 4.1.5 on 2023-01-15 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0004_alter_team_team"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="team",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="User.team"
            ),
        ),
    ]
