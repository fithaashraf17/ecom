# Generated by Django 4.0 on 2022-01-03 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_register_tb_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('passsword', models.TextField(default='')),
            ],
        ),
    ]
