from django.shortcuts import render

# Create your views here.

def player(request,id):
    content={''}
    return render(request,'player.html',content)