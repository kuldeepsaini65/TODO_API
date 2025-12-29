from api import views
from django.urls import path


app_name = 'api'
urlpatterns = [
     # -----------------
    # API Routes
    # -----------------
    path("tasks/", views.list_tasks_api, name="api_task_list"),
    path("tasks/create/", views.create_task_api, name="api_task_create"),
    path("tasks/<int:id>", views.task_info_api, name="api_task_create"),
    path("tasks/delete/<int:id>", views.task_delete_api, name="task_delete_api"),
    path("tasks/update/<int:id>", views.task_update_api, name="task_update_api"),
]
