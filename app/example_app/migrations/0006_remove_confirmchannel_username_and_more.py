# Generated by Django 5.1.1 on 2024-12-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0005_confirmchannel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmchannel',
            name='username',
        ),
        migrations.AlterField(
            model_name='confirmchannel',
            name='tg_id',
            field=models.BigIntegerField(unique=True),
        ),
    ]
