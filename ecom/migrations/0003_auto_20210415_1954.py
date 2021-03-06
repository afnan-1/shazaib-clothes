# Generated by Django 3.1.7 on 2021-04-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_auto_20210415_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='products', to='ecom.Product'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
