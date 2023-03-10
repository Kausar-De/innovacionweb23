# Generated by Django 4.0.1 on 2023-03-09 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userint', '0003_auto_20220329_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='levelchoice',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Advanced', 'Advanced')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='videolink',
            field=models.CharField(max_length=500, null=True, unique=True),
        ),
    ]
