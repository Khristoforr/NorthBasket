from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404


# Create your views here.
from django.views.generic import ListView

from statistic.models import Player, Game1, AverageStat

def show_main_page(request):
    best_scorer = AverageStat.objects.order_by('-pts')[0]
    best_blockshoter = AverageStat.objects.order_by('-blk')[0]
    best_rebounder = AverageStat.objects.order_by('-reb')[0]
    best_assister = AverageStat.objects.order_by('-ast')[0]
    best_stealer = AverageStat.objects.order_by('-stl')[0]
    context = {'best_scorer': best_scorer,
               'best_blockshoter':best_blockshoter,
               'best_rebounder': best_rebounder,
               'best_assister': best_assister,
               'best_stealer': best_stealer}
    return render(request, 'statistic/index.html', context=context)

def show_smth(request):
    player = Player.objects.order_by('-stats1__pts')[:5]
    context = {'players': player}
    return render(request, 'statistic/player.html', context=context)
    # return HttpResponse("Страница")

def show_player(request, player_name):
    return HttpResponse(f"Страница игрока {player_name}")

def show_team(request):
    return HttpResponse("Страница команды")

def pageNotFound(request, exception):
    return HttpResponseNotFound("Извините, но такой страницы не существует")

# class playerTest(ListView):
#     model = Player
#     template_name ='statistic/player.html'
#     context_object_name = 'player'
#
#     # def get_queryset(self):
#     #     return Player.objects.order_by('-stats1__pts')[:5]

# class playerTest(ListView):
#     model = Game1
#     template_name ='statistic/home.html'
#     context_object_name = 'players'
#
#
#     def get_queryset(self):
#         return AverageStat.objects.all().select_related('name').order_by('-min')[:5]
#
# def show_player(request, player_name):
#     player = get_object_or_404(Player, name=player_name)
#     context = {'player': player,
#                'title': player.name,
#                }
#     return render(request, 'statistic/home2.html', context=context)