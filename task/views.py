from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import TaskFrontendSerializers, TaskBackendSerializers


class TaskBackendViewSet(ModelViewSet):
    queryset = Task_Backend.objects.all()
    serializer_class = TaskBackendSerializers


class TaskFrontendViewSet(ModelViewSet):
    queryset = Task_Frontend.objects.all()
    serializer_class = TaskFrontendSerializers

