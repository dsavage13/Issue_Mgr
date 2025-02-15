# Generated by Django 5.1.5 on 2025-01-17 03:45

from django.db import migrations
from django.db.migrations import schemaeditor

def populate_status(apps, schemaeditor):
    status_entries = {
        "To-Do": "To-Do",
        "In Progress": "In Progress",
        "Completed": "Completed"
    }
    Status = apps.get_model("issues", "Status")
    for key, value in status_entries.items():
        status_obj = Status(name=key, description=value)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_auto_20250116_2137'),
    ]

    operations = [
        migrations.RunPython(populate_status)
    ]
