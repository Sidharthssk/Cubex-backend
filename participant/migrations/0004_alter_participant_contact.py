# Generated by Django 4.0.7 on 2022-11-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0003_rename_age_group_participant_agegroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='contact',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
