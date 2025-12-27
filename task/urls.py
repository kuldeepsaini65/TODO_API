from django.urls import path
from task.views import *

urlpatterns = [
    path('', index, name='index')
]
