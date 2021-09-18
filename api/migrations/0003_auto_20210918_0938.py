# Generated by Django 3.2.6 on 2021-09-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencybankingdeposit',
            name='depositor_id_number',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='agencybankingdeposit',
            name='depositor_id_type',
            field=models.CharField(blank=True, choices=[('Passport', 'Passport'), ('Voters Id', 'Voters Id'), ('Health Insurance', 'Health Insurance'), ('Driving License', 'Driving License'), ('Ghana National Card', 'Ghana National Card'), ('SSNIT Card', 'SSNIT Card')], max_length=100),
        ),
        migrations.AlterField(
            model_name='fraud',
            name='phone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
