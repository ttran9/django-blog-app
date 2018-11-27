from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        # https://docs.djangoproject.com/en/2.1/topics/signals/ (for explanation for this function).
        import users.signals
