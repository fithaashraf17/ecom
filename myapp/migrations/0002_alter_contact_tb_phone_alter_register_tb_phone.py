# Generated by Django 4.0 on 2021-12-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_tb',
            name='phone',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='register_tb',
            name='phone',
            field=models.CharField(default='', max_length=200),
        ),
    ]
