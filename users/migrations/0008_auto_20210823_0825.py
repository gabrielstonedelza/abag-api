# Generated by Django 3.2.6 on 2021-08-23 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210823_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='Abag User', max_length=150),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
