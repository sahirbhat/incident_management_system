# Generated by Django 4.1.7 on 2023-02-25 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_alter_incidents_incident_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='incident_id',
            field=models.CharField(default='RMG150172023', editable=False, max_length=15, unique=True),
        ),
    ]
