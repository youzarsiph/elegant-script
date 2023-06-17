""" AppConf """


from django.apps import AppConfig


class AsyncDjangoConfig(AppConfig):
    """ App configuration """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'async_django'
