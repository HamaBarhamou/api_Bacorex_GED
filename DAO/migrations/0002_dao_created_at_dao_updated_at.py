# Generated by Django 4.1.1 on 2022-09-18 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DAO', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dao',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 18, 11, 53, 27, 891676)),
        ),
        migrations.AddField(
            model_name='dao',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 18, 11, 53, 27, 891696)),
        ),
    ]
