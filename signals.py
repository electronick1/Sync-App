import datetime
from django.dispatch.dispatcher import receiver

from sync_app.apps import AppConfig

from .sync_hub import SyncHub
from .sync_hub import App

from.utils import TodoistAdapter, TodoistApi1, TodoistApi2

todoist_project_1 = App(TodoistAdapter(), TodoistApi1)
todoist_project_2 = App(TodoistAdapter(), TodoistApi2)

hub = SyncHub(todoist_project_1, todoist_project_2)


@receiver(AppConfig.signals.todoist_task_added)
def add_task(integration, obj, **kwargs):
     pass
