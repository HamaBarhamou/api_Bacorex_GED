# Generated by Django 4.1.1 on 2022-09-18 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DAO', '0007_dao_created_at_alter_dao_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dao',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 18, 12, 9, 12, 727325, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='dao',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 18, 12, 9, 12, 727394, tzinfo=datetime.timezone.utc)),
        ),
    ]
