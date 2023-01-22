# Generated by Django 4.1.5 on 2023-01-22 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Client", "0005_alter_client_sales_contact"),
        ("Event", "0003_alter_event_client_alter_event_event_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="Client.client"
            ),
        ),
    ]
