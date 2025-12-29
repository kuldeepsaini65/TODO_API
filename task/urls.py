from django.urls import path
from task import views

app_name = 'task'

urlpatterns = [

    # API Documentation
    path('api-docs', views.documentation, name = 'documentation'),


    # -----------------
    # Template Routes
    # -----------------
    path("", views.task_list_view, name="task_list"),
    path("tasks/add/", views.task_add_view, name="task_add"),
    path("tasks/info/<int:id>", views.task_info_view, name="task_info_view"),
    path("tasks/update/<int:id>", views.task_update_view, name="task_update_view"),
    # path("tasks/delete/<int:id>", views.task_delete_view, name="task_delete_view"),


   
]
