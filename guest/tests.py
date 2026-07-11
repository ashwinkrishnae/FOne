from django.test import TestCase
from django.urls import reverse

from .models import Message


class GuestTests(TestCase):
    def test_example(self):
        self.assertTrue(True)


class AdminDeletionTests(TestCase):
    def setUp(self):
        self.message = Message.objects.create(username="demo", message="hello world")

    def test_delete_single_message(self):
        session = self.client.session
        session["is_admin"] = True
        session.save()

        response = self.client.post(reverse("delete_message", args=[self.message.pk]))

        self.assertRedirects(response, reverse("admin_dashboard"))
        self.assertFalse(Message.objects.filter(pk=self.message.pk).exists())

    def test_delete_all_messages(self):
        session = self.client.session
        session["is_admin"] = True
        session.save()

        response = self.client.post(reverse("delete_all_messages"))

        self.assertRedirects(response, reverse("admin_dashboard"))
        self.assertEqual(Message.objects.count(), 0)
