# Generated by Django 3.2.6 on 2021-09-04 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_rename_other_phone_agencybankingdeposit_other_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencybankingregistration',
            name='account_number',
            field=models.CharField(default=0, max_length=13),
        ),
    ]
