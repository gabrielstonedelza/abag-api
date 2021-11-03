# Generated by Django 3.2.6 on 2021-11-03 08:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyBankingDeposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(choices=[('Access Bank', 'Access Bank'), ('Cal Bank', 'Cal Bank'), ('Fidelity Bank', 'Fidelity Bank'), ('Ecobank', 'Ecobank'), ('First Bank of Nigeria', 'First Bank of Nigeria'), ('SGSSB', 'SGSSB')], max_length=100)),
                ('beneficiary_account_number', models.CharField(max_length=15)),
                ('beneficiary_name', models.CharField(max_length=100)),
                ('depositor_number', models.CharField(max_length=15)),
                ('depositor_id_type', models.CharField(blank=True, choices=[('None', 'None'), ('Passport', 'Passport'), ('Voters Id', 'Voters Id'), ('Health Insurance', 'Health Insurance'), ('Driving License', 'Driving License'), ('Ghana National Card', 'Ghana National Card'), ('SSNIT Card', 'SSNIT Card')], default='', max_length=100)),
                ('depositor_id_number', models.CharField(blank=True, max_length=16)),
                ('amount', models.CharField(max_length=500)),
                ('date_deposited', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AgencyBankingRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(choices=[('Access Bank', 'Access Bank'), ('Cal Bank', 'Cal Bank'), ('Fidelity Bank', 'Fidelity Bank'), ('Ecobank', 'Ecobank'), ('First Bank of Nigeria', 'First Bank of Nigeria'), ('SGSSB', 'SGSSB')], default='GT Bank', max_length=100)),
                ('account_number', models.CharField(default=0, max_length=13)),
                ('phone', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('id_type', models.CharField(choices=[('None', 'None'), ('Passport', 'Passport'), ('Voters Id', 'Voters Id'), ('Health Insurance', 'Health Insurance'), ('Driving License', 'Driving License'), ('Ghana National Card', 'Ghana National Card'), ('SSNIT Card', 'SSNIT Card')], default='Ghana National Card', max_length=100)),
                ('id_number', models.CharField(max_length=16)),
                ('photo', models.ImageField(default='', upload_to='agency_abanking')),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AgencyBankingWithDraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(choices=[('Access Bank', 'Access Bank'), ('Cal Bank', 'Cal Bank'), ('Fidelity Bank', 'Fidelity Bank'), ('Ecobank', 'Ecobank'), ('First Bank of Nigeria', 'First Bank of Nigeria'), ('SGSSB', 'SGSSB')], max_length=100)),
                ('account_number', models.CharField(max_length=15)),
                ('amount', models.CharField(max_length=500)),
                ('date_withdrew', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AgentsAccountsCompletedWith',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physical_cash', models.IntegerField()),
                ('mtn_eCash', models.IntegerField()),
                ('vodafone_eCash', models.IntegerField()),
                ('airtel_tigo_eCash', models.IntegerField()),
                ('ecobank_eCash', models.IntegerField()),
                ('calbank_eCash', models.IntegerField()),
                ('fidelity_eCash', models.IntegerField()),
                ('date_closed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AgentsAccountsStartedWith',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physical_cash', models.IntegerField()),
                ('mtn_eCash', models.IntegerField()),
                ('vodafone_eCash', models.IntegerField()),
                ('airtel_tigo_eCash', models.IntegerField()),
                ('ecobank_eCash', models.IntegerField()),
                ('calbank_eCash', models.IntegerField()),
                ('fidelity_eCash', models.IntegerField()),
                ('date_started', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fraud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('reason', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MobileMoneyDeposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(choices=[('MTN', 'MTN'), ('VODAFONE', 'VODAFONE'), ('AIRTELTIGO', 'AIRTELTIGO')], max_length=11)),
                ('beneficiary_phone', models.CharField(max_length=15)),
                ('beneficiary_name', models.CharField(max_length=100)),
                ('depositor_phone', models.CharField(max_length=15)),
                ('depositor_id_type', models.CharField(blank=True, choices=[('None', 'None'), ('Passport', 'Passport'), ('Voters Id', 'Voters Id'), ('Health Insurance', 'Health Insurance'), ('Driving License', 'Driving License'), ('Ghana National Card', 'Ghana National Card'), ('SSNIT Card', 'SSNIT Card')], default='None', max_length=100)),
                ('depositor_number', models.CharField(blank=True, max_length=16)),
                ('amount', models.CharField(max_length=500)),
                ('date_deposited', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MobileMoneyUsersRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(choices=[('MTN', 'MTN'), ('VODAFONE', 'VODAFONE'), ('AIRTELTIGO', 'AIRTELTIGO')], default='MTN', max_length=11)),
                ('phone', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('id_type', models.CharField(choices=[('None', 'None'), ('Passport', 'Passport'), ('Voters Id', 'Voters Id'), ('Health Insurance', 'Health Insurance'), ('Driving License', 'Driving License'), ('Ghana National Card', 'Ghana National Card'), ('SSNIT Card', 'SSNIT Card')], default='Ghana National Card', max_length=100)),
                ('id_number', models.CharField(max_length=16)),
                ('photo', models.ImageField(default='', upload_to='mobile_money')),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MobileMoneyWithDraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(choices=[('MTN', 'MTN'), ('VODAFONE', 'VODAFONE'), ('AIRTELTIGO', 'AIRTELTIGO')], max_length=11)),
                ('phone', models.CharField(max_length=15)),
                ('amount', models.CharField(max_length=500)),
                ('date_withdrew', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MomoPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(choices=[('MTN', 'MTN'), ('VODAFONE', 'VODAFONE'), ('AIRTELTIGO', 'AIRTELTIGO')], max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('amount', models.CharField(max_length=500)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
