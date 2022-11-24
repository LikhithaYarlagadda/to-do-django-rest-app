from .views import task_create, task_list, task_detail, task_delete, task_update
from .models import Task
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .serializers import TaskSerializer


from rest_framework.response import Response

# initializing the APIClient app
client = Client()


class CreateTaskTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'title': 'Today Todos',
            'content': 'Get car wash',
            'completed': True
        }
        self.invalid_payload = {
            'invalid': 'invalid'
        }

    def test_create_valid_task(self):
        response = client.post(
            reverse(task_create),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_task(self):
        response = client.post(
            reverse(task_create),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TaskListTest(TestCase):
    def setUp(self):
        self.task_list = reverse(task_list)

    def test_get_task_list(self):
        response = self.client.get(self.task_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TaskDetailTest(TestCase):
    def setUp(self):
        self.test_task = Task.objects.create(title='new_task_title', content='new_task_content', completed=True)

    def test_get_task_detail(self):
        response = client.get(reverse(task_detail, kwargs={'pk': self.test_task.pk}))
        task = Task.objects.get(pk=self.test_task.pk)
        serializer = TaskSerializer(task)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TaskDeleteTest(TestCase):
    def setUp(self):
        self.test_task = Task.objects.create(title='new_task_title', content='new_task_content', completed=True)

    def test_delete_task(self):
        response = client.delete(reverse(task_delete, kwargs={'pk': self.test_task.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TaskUpdateTest(TestCase):
    def setUp(self):
        self.test_task = Task.objects.create(title='new_task_title', content='new_task_content', completed=True)
        self.update_payload = {
            'title': 'updated',
            'content': 'updated',
            'completed': True
        }

    def test_update_task(self):
        response = client.post(reverse(task_update, kwargs={'pk': self.test_task.pk}),
                               data=json.dumps(self.update_payload),
                               content_type='application/json'
                               )
        self.test_task.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.test_task.title, 'updated')


class TestTaskModel(TestCase):
    def test_model_str(self):
        title = Task.objects.create(title='title')
        self.assertEqual(str(title), 'title')
