# Generated by Django 3.1.7 on 2021-04-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0009_auto_20210416_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(blank=True, default=12),
            preserve_default=False,
        ),
    ]
