# Generated by Django 2.1.2 on 2018-12-23 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=30)),
                ('address2', models.CharField(max_length=30)),
                ('comment', models.TextField()),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('cancel_at', models.DateTimeField(null=True)),
            ],
        ),
    ]
