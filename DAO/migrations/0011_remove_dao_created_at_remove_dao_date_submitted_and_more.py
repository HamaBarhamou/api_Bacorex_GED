# Generated by Django 4.1.1 on 2022-09-19 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DAO', '0010_dao_description_dao_dao_id_dao_alter_dao_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dao',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='dao',
            name='date_submitted',
        ),
        migrations.RemoveField(
            model_name='dao',
            name='publication_date',
        ),
        migrations.RemoveField(
            model_name='dao',
            name='updated_at',
        ),
    ]