# Generated by Django 2.2.4 on 2020-03-06 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('felicia_app', '0003_auto_20200306_1454'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='catagory',
            new_name='category',
        ),
        migrations.RenameModel(
            old_name='subcatagory',
            new_name='subcategory',
        ),
    ]
