# Generated by Django 4.1 on 2022-08-31 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]