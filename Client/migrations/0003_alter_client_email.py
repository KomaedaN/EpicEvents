# Generated by Django 4.1.5 on 2023-01-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Client", "0002_rename_compagny_name_client_company_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client", name="email", field=models.EmailField(max_length=254),
        ),
    ]
