# Generated by Django 4.1 on 2022-08-31 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_question_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='voters',
            field=models.CharField(default=False, max_length=100),
        ),
    ]