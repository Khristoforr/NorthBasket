# Generated by Django 3.2.7 on 2021-10-16 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0003_auto_20211016_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='achievements',
            field=models.ManyToManyField(blank=True, null=True, through='statistic.Awards', to='statistic.Achievements'),
        ),
    ]
