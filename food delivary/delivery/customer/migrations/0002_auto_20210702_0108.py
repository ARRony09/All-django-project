# Generated by Django 3.2.4 on 2021-07-01 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='category',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='items',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.DeleteModel(
            name='OrderModel',
        ),
    ]
