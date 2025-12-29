from django.apps import AppConfig
from task.db_con import create_table

class TaskConfig(AppConfig):
    name = 'task'

    def ready(self):
        create_table()
