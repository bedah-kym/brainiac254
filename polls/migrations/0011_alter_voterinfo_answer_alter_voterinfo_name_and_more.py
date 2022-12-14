# Generated by Django 4.1 on 2022-08-31 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_alter_voterinfo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voterinfo',
            name='answer',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='voterinfo',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='voterinfo',
            name='poll_text',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.question'),
        ),
    ]
