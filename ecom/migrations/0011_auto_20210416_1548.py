# Generated by Django 3.1.7 on 2021-04-16 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0010_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
