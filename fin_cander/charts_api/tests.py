from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from finance.models import PeriodTime, Income, Plan, Expense


class TestCombinedData(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(username="testuser", password="testpassword")
		self.year = 2023
		self.month = 8

		user_obj = User.objects.get(username="testuser")
		period_obj = PeriodTime(year=2023, month=8).save()
		income_obj = Income(user=user_obj, date_period=period_obj, title_income="wyplata", amount_income=100).save()
		self.plan_obj = Plan(user=user_obj, date_period=period_obj, category_plan='Debt Payments', amount_plan=100).save()
		expense_obj = Expense(user=user_obj, date_period=period_obj, category_plan="Debt Payments", amount_expense=100).save()

	def test_combined_data(self):
		self.client.force_login(self.user)

		url = reverse("get_data", kwargs={'year': self.year, "month": self.month})
		response = self.client.get(url)

		self.assertEquals(response.status_code, status.HTTP_200_OK)
		self.assertIn("income_data", response.data)
		self.assertIn("plan_data", response.data)
		self.assertIn("expense_data", response.data)

	def test_total_view(self):
		self.client.force_login(self.user)

		url = reverse("total_view", kwargs={'year': self.year, 'month': self.month})
		response = self.client.get(url)

		self.assertEquals(response.status_code, status.HTTP_200_OK)
		self.assertIn("total_income", response.data)
		self.assertIn("total_plan", response.data)
		self.assertIn("total_expense", response.data)

	def test_detailed_plan_view(self):
		self.client.force_login(self.user)

		url = reverse("plan_view", kwargs={'year': self.year, 'month': self.month})
		response = self.client.get(url)

		self.assertEquals(response.status_code, status.HTTP_200_OK)
		self.assertIn("debt_payments", response.data)
		self.assertIn("investing", response.data)
		self.assertIn("saving", response.data)
		self.assertIn("housing", response.data)
		self.assertIn("food", response.data)
		self.assertIn("utilities", response.data)
		self.assertIn("medical", response.data)
		self.assertIn("personal_spending", response.data)
		self.assertIn("recreation", response.data)
		self.assertIn("miscellaneous", response.data)

	def test_detailed_expense_view(self):
		self.client.force_login(self.user)

		url = reverse("expense_view", kwargs={'year': self.year, 'month': self.month})
		response = self.client.get(url)

		self.assertEquals(response.status_code, status.HTTP_200_OK)
		self.assertIn("debt_payments", response.data)
		self.assertIn("investing", response.data)
		self.assertIn("saving", response.data)
		self.assertIn("housing", response.data)
		self.assertIn("food", response.data)
		self.assertIn("utilities", response.data)
		self.assertIn("medical", response.data)
		self.assertIn("personal_spending", response.data)
		self.assertIn("recreation", response.data)
		self.assertIn("miscellaneous", response.data)

	def test_delete_plan_view(self):
		self.client.force_login(self.user)

		url = reverse("delete_plan", kwargs={"plan_id": 1})
		response = self.client.delete(url)

		self.assertEquals(response.status_code, status.HTTP_200_OK)
		self.assertIn("state", response.data)

	def test_delete_income(self):
		self.client.force_login(self.user)

		url = reverse("delete-income", kwargs={"income_id": 1})
		response = self.client.delete(url)

		self.assertEquals(response.status_code, status.HTTP_200_OK)
		self.assertIn("state", response.data)

	def test_delete_expense(self):
		self.client.force_login(self.user)

		url = reverse("delete-expense", kwargs={"expense_id": 1})
		response = self.client.delete(url)

		self.assertEquals(response.status_code, status.HTTP_200_OK)
		self.assertIn("state", response.data)

"""""	def authenticate(self):
		self.client.post(reverse("register"), {
			'username': 'username',
			'email': 'email@gmail.com',
			'password': 'password'
		})

		response = self.client.post(
			reverse('login'), {'email': 'email@gmail.com',
							   'password': 'password'}
		)

		self.client.credentials(
			HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")"""


"""	def test_not_creates_todo(self):
		#self.authenticate()
		year = 2023
		month = 7

		url = reverse('get_data', args=[year, month])

		response = self.client.get(url)
		self.assertEquals(response.status_code, status.HTTP_200_OK)


"""