# Generated by Django 4.0.7 on 2022-11-18 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agegroup',
            name='event',
        ),
        migrations.AddField(
            model_name='agegroup',
            name='event',
            field=models.ManyToManyField(to='category.event'),
        ),
    ]