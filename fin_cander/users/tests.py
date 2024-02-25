from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

User_get = get_user_model()


class TestRegisterView(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.user_data = {
            "username": "testuser",
            "email": "testuser@wp.pl",
            "password1": "testpassword",
            "password2": "testpassword",
        }
        self.user_wrong_credentials = {
            "username": "testuser",
            "email": "testuser@wp.pl",
            "password1": "testpassword",
            "password2": "different_one",
        }

    def test_register_success(self):
        response = self.client.post(self.register_url, data=self.user_data, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertRedirects(response, self.login_url)
        self.assertTrue(
            User_get.objects.filter(username=self.user_data["username"]).exists()
        )

    def test_register_fail(self):
        response = self.client.post(
            self.register_url, self.user_wrong_credentials, follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(
            User_get.objects.filter(username=self.user_data["username"]).count() > 0
        )


class TestLoginView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("login")
        self.credentials = {"username": "testuser", "password": "testpassword"}
        self.wrong_credentials = {"username": "testuser", "password": "password"}

        self.user = User_get.objects.create_user(**self.credentials)

    def test_login_success(self):
        response = self.client.post(self.login_url, data=self.credentials, follow=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertRedirects(response, reverse("home_site"))
        self.assertTrue(response.context["user"].is_authenticated)

    def test_login_fail(self):
        response = self.client.post(
            self.login_url, data=self.wrong_credentials, follow=True
        )

        self.assertTrue(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.context["user"].is_authenticated)
