# Generated by Django 3.0.3 on 2020-03-18 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('felicia_app', '0006_auto_20200318_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.TextField(),
        ),
    ]