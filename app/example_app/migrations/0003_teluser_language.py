# Generated by Django 5.1.1 on 2024-12-03 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0002_teluser_delete_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='teluser',
            name='language',
            field=models.CharField(default='uz', max_length=255),
        ),
    ]
