from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_task_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('Task title must be at least 5 characters long.')
        return value
