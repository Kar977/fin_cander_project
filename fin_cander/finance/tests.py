from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from finance.models import PeriodTime


class Bugdeting(TestCase):

	def setUp(self):
		self.user = User.objects.create_user(username="testuser", password="testpassword")
		self.period = PeriodTime(year=2023, month=8).save()
		self.client.login(username="testuser", password="testpassword")

	def test_get_request(self):
		url = reverse("budgeting_first_view", kwargs={"year": 2023, "month": 8})
		response = self.client.get(url)

		self.assertEquals(response.status_code, status.HTTP_200_OK)

	def test_post_income(self):
		url = reverse("budgeting_first_view", kwargs={"year": 2023, "month": 8})

		user_input = {"title_income": "Wyplata testowa", "amount_income": 125, "date_income": "2013-08-08", "income_btn": True}
		response = self.client.post(url, data=user_input)

		self.assertEquals(response.status_code, status.HTTP_302_FOUND)

	def test_post_plan(self):
		url = reverse("budgeting_first_view", kwargs={"year": 2023, "month": 8})

		user_input = {"category_plan": "Debt Payments", "amount_plan": 521, "plan_btn": True}
		response = self.client.post(url, data=user_input)

		self.assertEquals(response.status_code, status.HTTP_302_FOUND)

	def test_post_expense(self):
		url = reverse("budgeting_first_view", kwargs={"year": 2023, "month": 8})

		user_input = {"category_plan": "Medical & Healthcare", "amount_expense": 111, "date_expense": "2023-08-09", "expense_btn": True}
		response = self.client.post(url, data=user_input)

		self.assertEquals(response.status_code, status.HTTP_302_FOUND)

