# Generated by Django 4.1.7 on 2023-02-24 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_incidents_incident_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='incident_id',
            field=models.CharField(default='RMG202380423', max_length=15, unique=True),
        ),
    ]