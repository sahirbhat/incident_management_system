# Generated by Django 4.1.7 on 2023-02-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_alter_incidents_id_alter_incidents_incident_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='incidents',
            name='incident_id',
            field=models.CharField(auto_created=True, default='RMG202322747', editable=False, max_length=15),
        ),
    ]
