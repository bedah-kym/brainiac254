# Generated by Django 4.1 on 2022-08-31 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_alter_voterinfo_answer_alter_voterinfo_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Voterinfo',
            new_name='Voteinfo',
        ),
    ]
