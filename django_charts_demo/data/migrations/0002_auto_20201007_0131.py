# Generated by Django 3.1.2 on 2020-10-07 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='payment',
            field=models.CharField(max_length=50),
        ),
    ]
