# Generated by Django 4.1.1 on 2022-09-18 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DAO', '0003_alter_dao_created_at_alter_dao_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dao',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 18, 11, 57, 5, 926477, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='dao',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 18, 11, 57, 5, 926502, tzinfo=datetime.timezone.utc)),
        ),
    ]
