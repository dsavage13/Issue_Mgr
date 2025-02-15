# Generated by Django 5.1.5 on 2025-01-17 02:00

from django.db import migrations

def populate_teams(apps, schemaeditor):
    teams_entries = {
        "Alpha": "The A team",
        "Bravo": "The B team",
        "Charlie": "The C team"
    }
    
    Team=apps.get_model("accounts", "Team")
    for key, value in teams_entries.items():
        teams_obj=Team(name=key, description=value)
        teams_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_teams)
    ]
