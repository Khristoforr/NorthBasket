# Generated by Django 3.2.7 on 2021-11-28 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0023_player_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='games_played',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.CreateModel(
            name='Game4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min', models.DecimalField(decimal_places=1, max_digits=10)),
                ('pts', models.DecimalField(decimal_places=1, max_digits=10)),
                ('fgm2', models.DecimalField(decimal_places=1, max_digits=10)),
                ('fga2', models.DecimalField(decimal_places=1, max_digits=10)),
                ('fg2', models.DecimalField(decimal_places=1, max_digits=10)),
                ('fgm3', models.DecimalField(decimal_places=1, max_digits=10)),
                ('fga3', models.DecimalField(decimal_places=1, max_digits=10)),
                ('fg3', models.DecimalField(decimal_places=1, max_digits=10)),
                ('fgm', models.DecimalField(decimal_places=1, max_digits=10)),
                ('fga', models.DecimalField(decimal_places=1, max_digits=10)),
                ('fg', models.DecimalField(decimal_places=1, max_digits=10)),
                ('ftm', models.DecimalField(decimal_places=1, max_digits=10)),
                ('fta', models.DecimalField(decimal_places=1, max_digits=10)),
                ('ft', models.DecimalField(decimal_places=1, max_digits=10)),
                ('oreb', models.DecimalField(decimal_places=1, max_digits=10)),
                ('dreb', models.DecimalField(decimal_places=1, max_digits=10)),
                ('reb', models.DecimalField(decimal_places=1, max_digits=10)),
                ('ast', models.DecimalField(decimal_places=1, max_digits=10)),
                ('tov', models.DecimalField(decimal_places=1, max_digits=10)),
                ('stl', models.DecimalField(decimal_places=1, max_digits=10)),
                ('blk', models.DecimalField(decimal_places=1, max_digits=10)),
                ('eff', models.DecimalField(decimal_places=1, max_digits=10)),
                ('plus_minus', models.DecimalField(decimal_places=1, max_digits=10)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats4', to='statistic.player')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
