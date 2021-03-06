# Generated by Django 4.0 on 2022-01-05 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_cart_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_tb',
            name='total',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='cart_tb',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product_tb'),
        ),
        migrations.AlterField(
            model_name='cart_tb',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.register_tb'),
        ),
        migrations.AlterField(
            model_name='product_tb',
            name='quantity',
            field=models.CharField(default='10', max_length=200),
        ),
    ]
