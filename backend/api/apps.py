"""Модуль приложений."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Приложение АПИ."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
