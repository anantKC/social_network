from django.apps import AppConfig


class SocialNetworkCoreAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'social_network_core_app'

    def ready(self):
        import social_network_core_app.signals
