from django.apps import AppConfig


class FilmConfig(AppConfig):
    name = 'film'
    def ready(self):
        import users.signals
