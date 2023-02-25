# Generated by Django 4.1.7 on 2023-02-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='incidents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_id', models.CharField(default='RMG*****202361229', max_length=15, unique=True)),
                ('reporter_name', models.TextField()),
                ('incident_details', models.TextField()),
                ('reported_date_time', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='medium', max_length=10)),
                ('incident_status', models.CharField(choices=[('open', 'Open'), ('progress', 'In Progress'), ('closed', 'Closed')], default='open', max_length=10)),
            ],
        ),
    ]