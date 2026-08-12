from datetime import date, timedelta

from django.test import TestCase
from todo.forms import TaskForm
from todo.models import Project


class TaskFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # We need a project to select in the form dropdown
        cls.project = Project.objects.create(name="Form Project")

    def test_valid_task_form(self):
        # 1. Create perfect data
        form = TaskForm(
            data={
                "project": self.project.id,
                "title": "Learn Forms",
                "description": "Form validation testing",
                "start_date": date.today(),
                "due_date": date.today() + timedelta(days=5),
                "is_completed": False,
            }
        )
        self.assertTrue(form.is_valid())

    def test_invalid_past_due_date(self):
        # 2. Trigger "Validation 1" by using a past due_date
        past_date = date.today() - timedelta(days=1)
        form = TaskForm(
            data={
                "project": self.project.id,
                "title": "Late Task",
                "description": "This should fail",
                "start_date": past_date,
                "due_date": past_date,
                "is_completed": False,
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("due_date", form.errors)
        self.assertEqual(
            form.errors["due_date"][0], "The due date cannot be in the past!"
        )

    def test_invalid_due_date_before_start_date(self):
        # 3. Trigger "Validation 2"
        start = date.today() + timedelta(days=5)
        due = date.today() + timedelta(days=2)  # Due BEFORE start!
        form = TaskForm(
            data={
                "project": self.project.id,
                "title": "Time Travel Task",
                "description": "This should fail",
                "start_date": start,
                "due_date": due,
                "is_completed": False,
            }
        )
        self.assertFalse(form.is_valid())
        # The 'clean' method assigns errors to '__all__' (non-field errors)
        self.assertIn("__all__", form.errors)
        self.assertEqual(
            form.errors["__all__"][0], "Due date must come after the start date."
        )
