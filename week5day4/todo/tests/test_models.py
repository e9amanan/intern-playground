from datetime import date

from django.test import TestCase
from todo.models import Project, Task


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.project = Project.objects.create(name="Django Mastery")

        cls.task = Task.objects.create(
            project=cls.project,
            title="Write Model Tests",
            description="Testing the core database structure.",
            start_date=date(2026, 8, 12),
            due_date=date(2026, 8, 20),
            is_completed=False,
        )

    def test_project_creation_and_str(self):

        self.assertEqual(self.project.name, "Django Mastery")
        self.assertEqual(str(self.project), "Django Mastery")

    def test_task_creation_and_str(self):

        self.assertEqual(self.task.title, "Write Model Tests")
        self.assertEqual(self.task.project, self.project)
        self.assertEqual(str(self.task), "Write Model Tests")
        self.assertFalse(self.task.is_completed)
