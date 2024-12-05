# Generated by Django 5.1.3 on 2024-12-03 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.BigIntegerField(unique=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('fullname', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
