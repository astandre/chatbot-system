from django.apps import AppConfig


class NluengineConfig(AppConfig):
    name = 'nluengine'

    # TODO train model
    def ready(self):
        print('Ready to train')