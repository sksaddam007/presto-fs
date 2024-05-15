from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    @swagger_auto_schema(operation_description="Create a new task")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(operation_description="Retrieve a task")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a task")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a task")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(operation_description="Register a new user")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
