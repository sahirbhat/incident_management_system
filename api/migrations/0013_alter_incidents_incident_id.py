# Generated by Django 4.1.7 on 2023-02-24 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_incidents_id_alter_incidents_incident_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='incident_id',
            field=models.CharField(auto_created=True, default='RMG202363370', editable=False, max_length=15, unique=True),
        ),
    ]
