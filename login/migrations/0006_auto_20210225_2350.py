# Generated by Django 3.1.7 on 2021-02-26 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20210225_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='friend',
            field=models.ManyToManyField(to='login.User'),
        ),
    ]
