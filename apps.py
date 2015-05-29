import environ
from powerapp.core.apps import ServiceAppConfig

env = environ.Env()


class AppConfig(ServiceAppConfig):
    name = "sync_app"
    verbose_name = "Integration github with todoist"
    models_module = "models"
