# Generated by Django 2.1.2 on 2018-12-21 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField(default=0)),
                ('count', models.PositiveIntegerField(default=0)),
                ('photos', models.ImageField(blank=True, upload_to='option')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_options', to='products.Product')),
            ],
        ),
    ]
