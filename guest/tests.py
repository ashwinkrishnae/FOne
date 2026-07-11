import importlib
import os

from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .models import Message


class GuestTests(TestCase):
    def test_example(self):
        self.assertTrue(True)


class DatabaseSettingsTests(SimpleTestCase):
    def test_postgres_database_url_is_used_when_available(self):
        original_database_url = os.environ.get("DATABASE_URL")
        os.environ["DATABASE_URL"] = "postgres://user:password@localhost:5432/followone"

        try:
            import config.settings as settings_module

            reloaded_settings = importlib.reload(settings_module)
            self.assertEqual(
                reloaded_settings.DATABASES["default"]["ENGINE"],
                "django.db.backends.postgresql",
            )
        finally:
            if original_database_url is None:
                os.environ.pop("DATABASE_URL", None)
            else:
                os.environ["DATABASE_URL"] = original_database_url


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
