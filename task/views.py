from django.shortcuts import render, HttpResponse




def index(request):
    return HttpResponse('<h1 style="color:red"><b>This is home page<b></h1>')
