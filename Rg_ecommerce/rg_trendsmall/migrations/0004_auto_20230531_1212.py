# Generated by Django 3.2.12 on 2023-05-31 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rg_trendsmall', '0003_laptops_oldprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptops',
            name='dicount_percentage',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='laptops',
            name='oldprice',
            field=models.IntegerField(null=True),
        ),
    ]