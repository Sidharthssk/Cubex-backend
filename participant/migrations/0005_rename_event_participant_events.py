# Generated by Django 4.1.2 on 2022-11-20 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0004_alter_participant_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='event',
            new_name='events',
        ),
    ]