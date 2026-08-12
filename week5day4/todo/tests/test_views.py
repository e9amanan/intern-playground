from datetime import date, timedelta

from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse
from todo.models import Project, Task


class TaskViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.project = Project.objects.create(name="View Project")
        cls.task = Task.objects.create(
            project=cls.project,
            title="Existing Task",
            description="To be updated",
            start_date=date.today(),
            due_date=date.today() + timedelta(days=1),
            is_completed=False,
        )
        # URLs based on the provided urls.py
        cls.create_url = reverse("task_create")
        cls.update_url = reverse("task_update", kwargs={"pk": cls.task.pk})

    def test_task_create_get(self):
        # 1. Test loading the create page
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/task_form.html")

    def test_task_create_post_success(self):
        # 2. Test submitting valid data to create a task
        data = {
            "project": self.project.id,
            "title": "New POST Task",
            "description": "Created via test client",
            "start_date": date.today(),
            "due_date": date.today() + timedelta(days=2),
            "is_completed": False,
        }
        response = self.client.post(self.create_url, data)

        # Verify redirect happens
        self.assertEqual(response.status_code, 302)
        # Verify the database grew
        self.assertEqual(Task.objects.count(), 2)

        # Verify the success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Task successfully created!")

    def test_task_update_post_success(self):
        # 3. Test submitting data to update an existing task
        data = {
            "project": self.project.id,
            "title": "Updated Title",
            "description": "Updated via test client",
            "start_date": date.today(),
            "due_date": date.today() + timedelta(days=10),
            "is_completed": True,
        }
        response = self.client.post(self.update_url, data)

        self.assertEqual(response.status_code, 302)

        # Refresh from db to get new values
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated Title")
        self.assertTrue(self.task.is_completed)
