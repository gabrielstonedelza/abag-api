# Generated by Django 3.2.6 on 2021-09-18 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210918_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='regional_code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
