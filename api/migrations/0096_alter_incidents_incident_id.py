# Generated by Django 4.1.7 on 2023-02-26 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0095_alter_incidents_incident_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='incident_id',
            field=models.CharField(default='RMG202386408', editable=False, max_length=15),
        ),
    ]
