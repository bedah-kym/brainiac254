# Generated by Django 4.1 on 2022-08-20 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choices',
            new_name='choice_text',
        ),
    ]
