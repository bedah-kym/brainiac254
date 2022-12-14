# Generated by Django 4.1 on 2022-08-31 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_remove_choice_voters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voteinfo',
            name='answer',
            field=models.CharField(default='not yet voted', max_length=200),
        ),
        migrations.AlterField(
            model_name='voteinfo',
            name='name',
            field=models.CharField(default='Empty', max_length=50),
        ),
        migrations.AlterField(
            model_name='voteinfo',
            name='poll_text',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='polls.question'),
            preserve_default=False,
        ),
    ]
