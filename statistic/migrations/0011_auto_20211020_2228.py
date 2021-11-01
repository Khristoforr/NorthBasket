# Generated by Django 3.2.7 on 2021-10-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0010_game3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='averagestat',
            name='ast',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='blk',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='dreb',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='eff',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fg',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fg2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fg3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fga',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fga2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fga3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fgm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fgm2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fgm3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='ft',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fta',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='ftm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='min',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='oreb',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='plus_minus',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='pts',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='reb',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='stl',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='tov',
            field=models.FloatField(),
        ),
    ]