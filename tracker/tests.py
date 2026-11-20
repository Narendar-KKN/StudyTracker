from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Task

class StudyTrackerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="learner", password="StrongPass123!")
        self.client.login(username="learner", password="StrongPass123!")

    def test_dashboard_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 302)

    def test_user_can_add_task(self):
        response = self.client.post(reverse("task_create"), {
            "title": "Revise Python",
            "description": "Practice Django basics",
            "due_date": "",
            "priority": "high",
        })
        self.assertRedirects(response, reverse("task_list"))
        self.assertEqual(Task.objects.filter(user=self.user).count(), 1)

    def test_users_only_see_their_own_tasks(self):
        other = User.objects.create_user(username="other", password="StrongPass123!")
        Task.objects.create(user=other, title="Private task")
        response = self.client.get(reverse("task_list"))
        self.assertNotContains(response, "Private task")
