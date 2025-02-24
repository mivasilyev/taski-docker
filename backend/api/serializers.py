"""Модуль сериализаторов АПИ."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор тасков."""

    class Meta:
        """Класс мета."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
