# Generated by Django 4.1.7 on 2023-02-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_alter_incidents_incident_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='incident_id',
            field=models.CharField(default='RMG422612023', editable=False, max_length=15, unique=True),
        ),
    ]
