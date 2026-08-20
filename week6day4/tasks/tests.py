from rest_framework.test import APITestCase,APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task

class TaskAPITestCase(APITestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='testguy',password='password123')

        self.client=APIClient()

        self.client.force_authenticate(user=self.user)

    def test_create_task(self):

        data={
            'title':'Automate everything',
            'description':'writing tests is fun',
        }

        response=self.client.post('/api/tasks/',data,format='json')

        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

        self.assertEqual(Task.objects.count(),1)

        self.assertEqual(Task.objects.get().owner,self.user)
        
