# Generated by Django 2.2.8 on 2019-12-03 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_board_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.CharField(max_length=255),
        ),
    ]