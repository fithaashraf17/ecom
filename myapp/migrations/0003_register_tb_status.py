# Generated by Django 4.0 on 2021-12-28 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_contact_tb_phone_alter_register_tb_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_tb',
            name='status',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
