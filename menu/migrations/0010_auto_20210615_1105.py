# Generated by Django 3.2 on 2021-06-15 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_auto_20210615_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
