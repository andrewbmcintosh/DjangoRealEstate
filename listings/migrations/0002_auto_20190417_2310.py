# Generated by Django 2.2 on 2019-04-17 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(),
        ),
    ]
