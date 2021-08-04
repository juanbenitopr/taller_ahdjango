from importlib import import_module
from typing import Optional

from django.apps import AppConfig


class CustomAppConfig(AppConfig):
    models_path: Optional[str] = None

    def import_models(self):
        self.models = self.apps.all_models[self.label]

        models_path = self.models_path or f'{self.label}.infrastructure.models'
        self.models_module = import_module(models_path)
