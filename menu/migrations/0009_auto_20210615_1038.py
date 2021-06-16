# Generated by Django 3.2 on 2021-06-15 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_alter_menu_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='price1',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='price2',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='price_tag',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AddField(
            model_name='menu',
            name='price_tag1',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AddField(
            model_name='menu',
            name='price_tag2',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.IntegerField(max_length=10),
        ),
    ]