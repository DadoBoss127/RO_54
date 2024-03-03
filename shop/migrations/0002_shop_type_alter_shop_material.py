# Generated by Django 5.0.2 on 2024-03-02 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='type',
            field=models.CharField(choices=[('rings', 'Rings'), ('necklaces', 'Necklaces'), ('earrings', 'Earrings'), ('bracelets', 'Bracelets'), ('anklets', 'Anklets'), ('sets', 'Sets'), ('other', 'Other')], default='rings', max_length=9),
        ),
        migrations.AlterField(
            model_name='shop',
            name='material',
            field=models.CharField(choices=[('gold', 'Gold'), ('silver', 'Silver'), ('platinum', 'Platinum'), ('bronze', 'Bronze'), ('other', 'Other')], default='gold', max_length=8),
        ),
    ]
