# Generated by Django 4.0 on 2022-01-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_payment_tb_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='email_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=200)),
                ('date', models.CharField(default='', max_length=200)),
            ],
        ),
    ]