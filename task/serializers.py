from rest_framework import serializers
from .models import *

class TaskBackendSerializers(serializers.ModelSerializer):

    class Meta:
        model = Task_Backend
        fields = '__all__'


class TaskFrontendSerializers(serializers.ModelSerializer):

    class Meta:
        model = Task_Frontend
        fields = '__all__'