# Generated by Django 4.1.7 on 2023-02-25 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0091_alter_incidents_incident_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidents',
            name='id',
            field=models.IntegerField(auto_created=True, default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='incidents',
            name='incident_id',
            field=models.CharField(default='RMG202373402', editable=False, max_length=15),
        ),
    ]
