# Generated by Django 5.0.2 on 2024-03-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shop',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
