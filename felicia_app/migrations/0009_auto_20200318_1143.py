# Generated by Django 3.0.3 on 2020-03-18 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('felicia_app', '0008_auto_20200318_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
    ]
