from django.contrib.auth import views as auth_views
from django.test import TestCase, Client
from django.urls import reverse, resolve

from charts_api.views import (
	CombinedData,
	TotalViewData,
	DetailedPlanViewData,
	DetailedExpenseViewData,
	DeletePlan,
	DeleteExpense,
	DeleteIncome
)
from finance.views.income.crud import CreateIncomePlanExecuteFirstView
from users.views import RegisterView, profile
from website.views import HomeView

client = Client()


class TestHomeView(TestCase):

	def test_should_return_200_when_is_called(self):
		expected_status_code = 200
		response = client.get("/home/")
		actual_status_code = response.status_code
		print(actual_status_code)
		self.assertEquals(expected_status_code, actual_status_code)


class TestUrls(TestCase):

	def test_home_url_is_resolved(self):
		url = reverse('home_site')
		print(url)
		self.assertEquals(resolve(url).func.view_class, HomeView)

	def test_register_url_is_resolved(self):
		url = reverse('register')
		self.assertEquals(resolve(url).func.view_class, RegisterView)

	def test_login_url_is_resolved(self):
		url = reverse('login')
		self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)

	def test_logout_url_is_resolved(self):
		url = reverse('logout')
		self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)

	def test_budgeting_url_is_resolved(self):
		year = 2023
		month = 8

		url = reverse('budgeting_first_view', args=(year, month))
		self.assertEquals(resolve(url).func.view_class, CreateIncomePlanExecuteFirstView)

	def test_profile_url_is_resolved(self):
		url = reverse('profile')
		self.assertEquals(resolve(url).func, profile)

	def test_api_combined_data_url_is_resolve(self):
		year = 2023
		month = 5

		url = reverse('get_data', args=(year, month))
		self.assertEquals(resolve(url).func.view_class, CombinedData)

	def test_api_total_view_data_url_is_resolve(self):
		year = 2023
		month = 5

		url = reverse('total_view', args=(year, month))
		self.assertEquals(resolve(url).func.view_class, TotalViewData)

	def test_api_detailed_plan_view_data_url_is_resolved(self):
		year = 2023
		month = 5

		url = reverse('plan_view', args=(year, month))
		self.assertEquals(resolve(url).func.view_class, DetailedPlanViewData)

	def test_api_detailed_expense_view_data_url_is_resolved(self):
		year = 2023
		month = 5

		url = reverse('expense_view', args=(year, month))
		self.assertEquals(resolve(url).func.view_class, DetailedExpenseViewData)

	def test_api_delete_plan_url_is_resolved(self):
		plan_id = [1]

		url = reverse('delete_plan', args=plan_id)
		self.assertEquals(resolve(url).func.view_class, DeletePlan)

	def test_api_delete_income_url_is_resolved(self):
		income_id = [1]

		url = reverse('delete-income', args=income_id)
		self.assertEquals(resolve(url).func.view_class, DeleteIncome)

	def test_api_delete_expense_url_is_resolved(self):
		expense_id = [1]

		url = reverse('delete-expense', args=expense_id)
		self.assertEquals(resolve(url).func.view_class, DeleteExpense)
