# Generated by Django 3.1.11 on 2021-07-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('useename', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
