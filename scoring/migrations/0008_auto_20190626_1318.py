# Generated by Django 2.1.7 on 2019-06-26 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0007_event_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='short_name',
            field=models.CharField(default='', max_length=64),
        ),
    ]
