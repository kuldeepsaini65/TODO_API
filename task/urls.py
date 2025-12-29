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
    path("tasks/delete/<int:id>", views.task_delete_view, name="task_delete_view"),


    # -----------------
    # API Routes
    # -----------------
    path("api/tasks/", views.list_tasks_api, name="api_task_list"),
    path("api/tasks/create/", views.create_task_api, name="api_task_create"),
    path("api/tasks/<int:id>", views.task_info_api, name="api_task_create"),
    path("api/tasks/delete/<int:id>", views.task_delete_api, name="task_delete_api"),
    path("api/tasks/update/<int:id>", views.task_update_api, name="task_update_api"),
]
