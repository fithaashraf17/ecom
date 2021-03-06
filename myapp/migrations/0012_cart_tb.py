# Generated by Django 4.0 on 2022-01-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_product_tb_quantity_alter_product_tb_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(default='', max_length=200)),
                ('user_id', models.CharField(default='', max_length=200)),
                ('quantity', models.CharField(default='', max_length=200)),
                ('price', models.CharField(default='', max_length=200)),
                ('status', models.CharField(default='pending', max_length=200)),
            ],
        ),
    ]
