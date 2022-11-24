from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

"""

API Overview

"""


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/task_list/',
        'Detail View': '/task_detail/<str:pk>/',
        'Create': '/task_create/',
        'Update': '/task_update/<str:pk>/',
        'Delete': '/task_delete/<str:pk>/',
    }
    return Response(api_urls)


"""

This function below will show the entire task repository in the database.

"""


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


"""

This function will show the detailed view of a specific task with the help of pk.

"""


@api_view(['GET'])
def task_detail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'completed': request.data.get('completed')
        }
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def task_update(request, pk):
    task = Task.objects.get(id=int(pk))
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Task deleted successfully.")
