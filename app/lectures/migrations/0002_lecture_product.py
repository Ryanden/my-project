# Generated by Django 2.1.2 on 2018-12-12 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('lectures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='products.Product'),
        ),
    ]
