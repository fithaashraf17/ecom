# Generated by Django 4.0 on 2022-01-05 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_cart_tb_total_alter_cart_tb_product_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_tb',
            name='quantity',
            field=models.CharField(default='', max_length=200),
        ),
    ]
