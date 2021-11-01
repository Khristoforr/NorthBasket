import xlrd
from django.core.management.base import BaseCommand
from statistic.models import Player, Game1, Game2, Game3, AverageStat
from django.db import connection


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):
        AverageStat.objects.all().delete()
        x = int(input("Введите кол-во игр"))
        game_list = [Game1, Game2, Game3]
        not_empty_stats = game_list[0:(x)]

        for player in range(len(Game1.objects.all())):
            some_player = AverageStat(name_id=Game1.objects.all()[player].name,
                                      min=sum([i.objects.all()[player].min for i in not_empty_stats])/len(not_empty_stats),
                                      pts=sum([i.objects.all()[player].pts for i in not_empty_stats])/len(not_empty_stats),
                                      fgm2=sum([i.objects.all()[player].fgm2 for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      fga2=sum([i.objects.all()[player].fga2 for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      fg2=sum([i.objects.all()[player].fg2 for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      fgm3=sum([i.objects.all()[player].fgm3 for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      fga3=sum([i.objects.all()[player].fga3 for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      fg3=sum([i.objects.all()[player].fg3 for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      fgm=sum([i.objects.all()[player].fgm for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      fga=sum([i.objects.all()[player].fga for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      fg=sum([i.objects.all()[player].fg for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      ftm=sum([i.objects.all()[player].ftm for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      fta=sum([i.objects.all()[player].fta for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      ft=sum([i.objects.all()[player].ft for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      oreb=sum([i.objects.all()[player].oreb for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      dreb=sum([i.objects.all()[player].dreb for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      reb=sum([i.objects.all()[player].reb for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      ast=sum([i.objects.all()[player].ast for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      tov=sum([i.objects.all()[player].tov for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      stl=sum([i.objects.all()[player].stl for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      blk=sum([i.objects.all()[player].blk for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      eff=sum([i.objects.all()[player].eff for i in not_empty_stats]) / len(
                                          not_empty_stats),
                                      plus_minus=sum([i.objects.all()[player].plus_minus for i in not_empty_stats]) / len(
                                          not_empty_stats))
            some_player.save()
