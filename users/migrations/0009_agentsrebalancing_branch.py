# Generated by Django 3.2.6 on 2021-09-07 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210823_0825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('user_code', models.CharField(max_length=11, unique=True)),
                ('full_name', models.CharField(default='Abag Agent User', max_length=150)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AgentsRebalancing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('agent1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requesting_agent', to=settings.AUTH_USER_MODEL)),
                ('agent2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accepting_agent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
