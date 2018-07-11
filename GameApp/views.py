from django.http import HttpResponse
from django.shortcuts import render
from .models import GameModel

# Create your views here.
def index(request):
    return  render(request,'GameApp/index.html')

def Gry(request):
    Gry=GameModel.objects.order_by('GameName')
    context={'Gry':Gry}
    return render(request,'GameApp/main.html',context)