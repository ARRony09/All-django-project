# Generated by Django 3.1.11 on 2021-07-02 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20210702_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year_of_production',
            field=models.DateField(),
        ),
    ]
