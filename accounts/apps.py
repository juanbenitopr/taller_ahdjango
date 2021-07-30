from importlib import import_module

from shared.infrastructure.django.custom_app_config import CustomAppConfig


class AccountsConfig(CustomAppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def import_models(self):
        self.models = self.apps.all_models[self.label]

        models_path = self.models_path or f'{self.label}.infrastructure.models'
        self.models_module = import_module(models_path)
