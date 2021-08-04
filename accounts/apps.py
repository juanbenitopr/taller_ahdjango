from shared.infrastructure.django.custom_app_config import CustomAppConfig


class AccountsConfig(CustomAppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

