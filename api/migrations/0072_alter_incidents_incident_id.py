# Generated by Django 4.1.7 on 2023-02-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0071_alter_incidents_incident_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='incident_id',
            field=models.CharField(auto_created=True, default='RMG668912023', editable=False, max_length=15),
        ),
    ]