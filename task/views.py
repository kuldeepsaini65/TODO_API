from django.shortcuts import render, HttpResponse
import json
import logging
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from task.db_con import *
from django.db import connection
import requests
from django.contrib import messages
from django.conf import settings

def documentation(request):
    return render(request, 'docs.html')


'''
Assignemt described HTML Templates will use API end Points,
So, Simply Means only render Templtes.
'''

def task_list_view(request):
    return render(request, "tasks/task_list.html")



def task_add_view(request):
    return render(request, "tasks/task_add.html")



def task_info_view(request, id):
    context ={}
    context["task_id"] = id
    return render(request, 'tasks/task_info.html', context)


def task_update_view(request, id):
    context = {}
    context["task_id"] = id
    return render(request, "tasks/task_add.html", context)
