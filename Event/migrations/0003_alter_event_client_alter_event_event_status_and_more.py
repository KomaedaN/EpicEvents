# Generated by Django 4.1.5 on 2023-01-19 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Client", "0005_alter_client_sales_contact"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Event", "0002_eventstatus_event_event_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="client",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT, to="Client.client"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="event_status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="Event.eventstatus"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="support_contact",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]