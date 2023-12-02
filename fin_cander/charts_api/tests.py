from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from django.utils import timezone
from rest_framework.test import APITestCase

from finance.models import PeriodTime, Income, Plan, Expense


class TestCombinedData(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.year = timezone.now().year
        self.month = timezone.now().month

        user_obj = User.objects.get(username="testuser")
        period_obj = PeriodTime.objects.create(year=self.year, month=self.month)

        self.amount_income = 100
        self.amount_plan = 105
        self.amount_expense = 110

        self.income_obj = Income.objects.create(
            user=user_obj,
            date_period=period_obj,
            title_income="wyplata",
            amount_income=self.amount_income,
        )
        self.plan_obj = Plan.objects.create(
            user=user_obj,
            date_period=period_obj,
            category_plan="Debt Payments",
            amount_plan=self.amount_plan,
        )
        self.expense_obj = Expense.objects.create(
            user=user_obj,
            date_period=period_obj,
            category_plan="Debt Payments",
            amount_expense=self.amount_expense,
        )

    def test_combined_data(self):
        self.client.force_login(self.user)

        url = reverse("get_data", kwargs={"year": self.year, "month": self.month})
        response = self.client.get(url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertIn("income_data", response.data)
        self.assertIn("plan_data", response.data)
        self.assertIn("expense_data", response.data)

        expected_value_income = self.amount_income
        dictionary_income = response.data["income_data"]
        final_value_income = dictionary_income[0]["amount_income"]

        self.assertEquals(expected_value_income, final_value_income)

        expected_value_plan = self.amount_plan
        dictionary_plan = response.data["plan_data"]
        final_value_plan = dictionary_plan[0]["amount_plan"]

        self.assertEquals(expected_value_plan, final_value_plan)

        expected_value_expense = self.amount_expense
        dictionary_expense = response.data["expense_data"]
        final_value_expense = dictionary_expense[0]["amount_expense"]

        self.assertEquals(expected_value_expense, final_value_expense)

    def test_total_view(self):
        self.client.force_login(self.user)

        url = reverse("total_view", kwargs={"year": self.year, "month": self.month})
        response = self.client.get(url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertIn("total_income", response.data)
        self.assertIn("total_plan", response.data)
        self.assertIn("total_expense", response.data)

    def test_detailed_plan_view(self):
        self.client.force_login(self.user)

        url = reverse("plan_view", kwargs={"year": self.year, "month": self.month})
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

        url = reverse("expense_view", kwargs={"year": self.year, "month": self.month})
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
        self.assertEquals(response.data["state"], "deleted")
        self.assertEquals(Plan.objects.filter(id=1).count(), 0)

    def test_delete_income(self):
        self.client.force_login(self.user)

        url = reverse("delete-income", kwargs={"income_id": 1})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertIn("state", response.data)
        self.assertEquals(Income.objects.filter(id=1).count(), 0)

    def test_delete_expense(self):
        self.client.force_login(self.user)

        url = reverse("delete-expense", kwargs={"expense_id": 1})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertIn("state", response.data)
        self.assertEquals(Expense.objects.filter(id=1).count(), 0)
