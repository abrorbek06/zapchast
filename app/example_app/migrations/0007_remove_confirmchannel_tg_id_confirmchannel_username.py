# Generated by Django 5.1.1 on 2024-12-03 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0006_remove_confirmchannel_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmchannel',
            name='tg_id',
        ),
        migrations.AddField(
            model_name='confirmchannel',
            name='username',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
