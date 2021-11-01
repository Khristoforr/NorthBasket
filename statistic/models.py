from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.TextField(primary_key=True, unique=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True, related_name='get_players')
    achievements = models.ManyToManyField('Achievements', through='Awards', null=True, blank=True)
    photo = models.ImageField(upload_to=f'photos/%Y/%m/%d/', verbose_name="фото", null=True, blank=True)
    rus_first_name = models.TextField()
    rus_last_name = models.TextField()
    injured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.TextField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    image = models.ImageField(upload_to=f'team_logo/%Y/%m/%d/', verbose_name="фото", null=True, blank=True)

    def __str__(self):
        return self.name


class Achievements(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

class Stat(models.Model):
    min = models.DecimalField(max_digits=10,decimal_places=1)
    pts = models.DecimalField(max_digits=10,decimal_places=1)
    fgm2 = models.DecimalField(max_digits=10,decimal_places=1)
    fga2 = models.DecimalField(max_digits=10,decimal_places=1)
    fg2 = models.DecimalField(max_digits=10,decimal_places=1)
    fgm3 = models.DecimalField(max_digits=10,decimal_places=1)
    fga3 = models.DecimalField(max_digits=10,decimal_places=1)
    fg3 = models.DecimalField(max_digits=10,decimal_places=1)
    fgm = models.DecimalField(max_digits=10,decimal_places=1)
    fga = models.DecimalField(max_digits=10,decimal_places=1)
    fg = models.DecimalField(max_digits=10,decimal_places=1)
    ftm = models.DecimalField(max_digits=10,decimal_places=1)
    fta = models.DecimalField(max_digits=10,decimal_places=1)
    ft = models.DecimalField(max_digits=10,decimal_places=1)
    oreb = models.DecimalField(max_digits=10,decimal_places=1)
    dreb = models.DecimalField(max_digits=10,decimal_places=1)
    reb = models.DecimalField(max_digits=10,decimal_places=1)
    ast = models.DecimalField(max_digits=10,decimal_places=1)
    tov = models.DecimalField(max_digits=10,decimal_places=1)
    stl = models.DecimalField(max_digits=10,decimal_places=1)
    blk = models.DecimalField(max_digits=10,decimal_places=1)
    eff = models.DecimalField(max_digits=10,decimal_places=1)
    plus_minus = models.DecimalField(max_digits=10,decimal_places=1)

    class Meta:
        abstract = True

class Game1(Stat):
    name = models.ForeignKey('Player', on_delete=models.CASCADE, to_field='name', related_name='stats1')


class Game2(Stat):
    name = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='stats2')


class Game3(Stat):
    name = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='stats3')

class AverageStat(Stat):
    name = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='avg_stats')


class Awards(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    achievement = models.ForeignKey('Achievements', on_delete=models.CASCADE)
    year_awarded = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.player} имеет награду {self.achievement}'