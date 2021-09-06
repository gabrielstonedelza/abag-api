# Generated by Django 3.2.6 on 2021-09-05 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0013_auto_20210905_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('date_messaged', models.DateTimeField(auto_now_add=True)),
                ('agent1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messenger1', to=settings.AUTH_USER_MODEL)),
                ('agent2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messenger2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
