import xlrd
from django.core.management.base import BaseCommand
from statistic.models import Player, Game1, Game2, Game3


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def calculate_fg(self, fgm, fga):
        if int(fga) == 0:
            return 0
        else:
            return (int(fgm)/int(fga)) * 100

    def handle(self, *args, **options):
        game_book = {1: 'first_game_stats.xlsx', 2: 'second_game_stats.xlsx', 3: 'third_game_stats.xlsx'}
        models_book = {1: Game1, 2: Game2, 3: Game3}
        admin_choise = int(input('Введите номер игры для импорта в БД'))
        workbook = xlrd.open_workbook(game_book[admin_choise], on_demand=True).sheet_by_index(0)
        first_row = []
        for col in range(workbook.ncols):
            first_row.append(workbook.cell_value(0, col))
        data = []
        for row in range(1, workbook.nrows):
            elm = {}
            for col in range(workbook.ncols):
                elm[first_row[col]] = workbook.cell_value(row, col)
            data.append(elm)

        for player in data:
            some_player = models_book[admin_choise](name_id=Player.objects.filter(name=player['Player'])[0].name,
                                 min=player['MIN'],
                                 pts=player['PTS'],
                                 fgm2=player['2PM'],
                                 fga2=player['2PA'],
                                 fg2=self.calculate_fg(player['2PM'],player['2PA']),
                                 fgm3=player['3PM'],
                                 fga3=player['3PA'],
                                 fg3=self.calculate_fg(player['3PM'],player['3PA']),
                                 fgm=player['FGM'],
                                 fga=player['FGA'],
                                 fg=self.calculate_fg(player['FGM'],player['FGA']),
                                 ftm=player['FTM'],
                                 fta=player['FTA'],
                                 ft=self.calculate_fg(player['FTM'],player['FTA']),
                                 oreb=player['OREB'],
                                 dreb=player['DREB'],
                                 reb=player['REB'],
                                 ast=player['AST'],
                                 tov=player['TOV'],
                                 stl=player['STL'],
                                 blk=player['BLK'],
                                 eff=player['EFF'],
                                 plus_minus=player['+/-']
                                     )
            some_player.save()
        print("Экспорт данных выполнен успешно")
