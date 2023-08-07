from rest_framework import generics
from django.shortcuts import render
from finance.models import PeriodTime, Income, Plan, Expense, User
from .serializers import PeriodTimeSerializer, IncomeSerializer, UserSerializer, PlanSerializer, ExpenseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum


"""class GetPeriodData(generics.ListAPIView):
	serializer_class = PeriodTimeSerializer
	queryset = PeriodTime.objects.all()

	def get_queryset(self):
		queryset = super().get_queryset()

		year = self.kwargs.get("year")
		month = self.kwargs.get("month")
		# TODO zastosowac logike wyszukiwania danych per model nastepnie polaczyc je i zwrocic do queryseta
		return queryset.filter(year=year, month=month)

# list api znalexc przyklad get api view z get_quesyster


class GetIncomeData(generics.ListAPIView):
	serializer_class = IncomeSerializer
	queryset = Income.objects.all()

	def get_queryset(self):
		queryset = super().get_queryset()

		return queryset.filter()"""


class CombinedData(APIView):
	def get(self, request, *args, **kwargs):

		current_user = self.request.user

		year = int(self.kwargs.get("year"))
		month = int(self.kwargs.get("month"))

		period_obj = PeriodTime.objects.get(year=year, month=month)
		queryset_income = Income.objects.filter(user=current_user, date_period=period_obj)
		queryset_plan = Plan.objects.filter(user=current_user, date_period=period_obj)
		queryset_expense = Expense.objects.filter(user=current_user, date_period=period_obj)

		serializer_income = IncomeSerializer(queryset_income, many=True)
		serializer_plan = PlanSerializer(queryset_plan, many=True)
		serializer_expense = ExpenseSerializer(queryset_expense, many=True)

		combined_data = {
			'income_data': serializer_income.data,
			'plan_data': serializer_plan.data,
			'expense_data': serializer_expense.data
		}

		return Response(combined_data)


class ToalViewData(APIView):
	def get(self, request, *args, **kwargs):

		current_user = self.request.user

		year = int(self.kwargs.get("year"))
		month = int(self.kwargs.get("month"))

		try:
			period_obj = PeriodTime.objects.get(year=year, month=month)
		except PeriodTime.DoesNotExist:
			combined_data = {
				'total_income': 0,
				'total_plan': 0,
				'total_expense': 0
			}

			return Response(combined_data)

		total_income = Income.objects.filter(user=current_user, date_period=period_obj).aggregate(Sum("amount_income"))["amount_income__sum"]
		total_plan = Plan.objects.filter(user=current_user, date_period=period_obj).aggregate(Sum("amount_plan"))["amount_plan__sum"]
		total_expense = Expense.objects.filter(user=current_user, date_period=period_obj).aggregate(Sum("amount_expense"))["amount_expense__sum"]

		combined_data = {
			'total_income': total_income,
			'total_plan': total_plan,
			'total_expense': total_expense
		}

		return Response(combined_data)


# TODO stworzyć klase które będzie zwracała w API info na temat Plan i drugi dla Expense


class DetailedPlanViewData(APIView):
	def get(self, request, *args, **kwargs):
		current_user = self.request.user

		year = int(self.kwargs.get("year"))
		month = int(self.kwargs.get("month"))

		try:
			period_obj = PeriodTime.objects.get(year=year, month=month)
		except PeriodTime.DoesNotExist:
			combined_plan_data = {
				'debt_payments': 0,
				'investing': 0,
				'saving': 0,
				'housing': 0,
				'food': 0,
				'utilities': 0,
				'medical': 0,
				'personal_spending': 0,
				'recreation': 0,
				'miscellaneous': 0
			}

			return Response(combined_plan_data)

		debt_payments = Plan.objects.filter(user=current_user, date_period=period_obj, category_plan="Debt Payments").aggregate(Sum("amount_plan"))["amount_plan__sum"]
		investing = Plan.objects.filter(user=current_user, date_period=period_obj, category_plan="Investing").aggregate(Sum("amount_plan"))["amount_plan__sum"]
		saving = Plan.objects.filter(user=current_user, date_period=period_obj, category_plan="Saving").aggregate(Sum("amount_plan"))["amount_plan__sum"]
		housing = Plan.objects.filter(user=current_user, date_period=period_obj, category_plan="Housing").aggregate(Sum("amount_plan"))["amount_plan__sum"]
		food = Plan.objects.filter(user=current_user, date_period=period_obj, category_plan="Food").aggregate(Sum("amount_plan"))["amount_plan__sum"]
		utilities = Plan.objects.filter(user=current_user, date_period=period_obj, category_plan="Utilities").aggregate(Sum("amount_plan"))["amount_plan__sum"]
		medical = Plan.objects.filter(user=current_user, date_period=period_obj, category_plan="Medical & Healthcare").aggregate(Sum("amount_plan"))["amount_plan__sum"]
		personal_spending = Plan.objects.filter(user=current_user, date_period=period_obj, category_plan="Personal Spending").aggregate(Sum("amount_plan"))["amount_plan__sum"]
		recreation = Plan.objects.filter(user=current_user, date_period=period_obj, category_plan="Recreation & Entertainment").aggregate(Sum("amount_plan"))["amount_plan__sum"]
		miscellaneous = Plan.objects.filter(user=current_user, date_period=period_obj, category_plan="Miscellaneous").aggregate(Sum("amount_plan"))["amount_plan__sum"]

		combined_plan_data = {
			'debt_payments': debt_payments,
			'investing': investing,
			'saving': saving,
			'housing': housing,
			'food': food,
			'utilities': utilities,
			'medical': medical,
			'personal_spending': personal_spending,
			'recreation': recreation,
			'miscellaneous': miscellaneous
		}

		for category in combined_plan_data:
			if 'None' in str(combined_plan_data.get(category)):
				combined_plan_data[category] = 0

		return Response(combined_plan_data)


class DetailedExpenseViewData(APIView):
	def get(self, request, *args, **kwargs):
		current_user = self.request.user

		year = int(self.kwargs.get("year"))
		month = int(self.kwargs.get("month"))

		try:
			period_obj = PeriodTime.objects.get(year=year, month=month)
		except PeriodTime.DoesNotExist:
			combined_expense_data = {
				'debt_payments': 0,
				'investing': 0,
				'saving': 0,
				'housing': 0,
				'food': 0,
				'utilities': 0,
				'medical': 0,
				'personal_spending': 0,
				'recreation': 0,
				'miscellaneous': 0
			}

			return Response(combined_expense_data)

		debt_payments = Expense.objects.filter(user=current_user, date_period=period_obj, category_plan="Debt Payments").aggregate(Sum("amount_expense"))["amount_expense__sum"]
		investing = Expense.objects.filter(user=current_user, date_period=period_obj, category_plan="Investing").aggregate(Sum("amount_expense"))["amount_expense__sum"]
		saving = Expense.objects.filter(user=current_user, date_period=period_obj, category_plan="Saving").aggregate(Sum("amount_expense"))["amount_expense__sum"]
		housing = Expense.objects.filter(user=current_user, date_period=period_obj, category_plan="Housing").aggregate(Sum("amount_expense"))["amount_expense__sum"]
		food = Expense.objects.filter(user=current_user, date_period=period_obj, category_plan="Food").aggregate(Sum("amount_expense"))["amount_expense__sum"]
		utilities = Expense.objects.filter(user=current_user, date_period=period_obj, category_plan="Utilities").aggregate(Sum("amount_expense"))["amount_expense__sum"]
		medical = Expense.objects.filter(user=current_user, date_period=period_obj, category_plan="Medical & Healthcare").aggregate(Sum("amount_expense"))["amount_expense__sum"]
		personal_spending = Expense.objects.filter(user=current_user, date_period=period_obj, category_plan="Personal Spending").aggregate(Sum("amount_expense"))["amount_expense__sum"]
		recreation = Expense.objects.filter(user=current_user, date_period=period_obj, category_plan="Recreation & Entertainment").aggregate(Sum("amount_expense"))["amount_expense__sum"]
		miscellaneous = Expense.objects.filter(user=current_user, date_period=period_obj, category_plan="Miscellaneous").aggregate(Sum("amount_expense"))["amount_expense__sum"]

		combined_expense_data = {
			'debt_payments': debt_payments,
			'investing': investing,
			'saving': saving,
			'housing': housing,
			'food': food,
			'utilities': utilities,
			'medical': medical,
			'personal_spending': personal_spending,
			'recreation': recreation,
			'miscellaneous': miscellaneous
		}

		for category in combined_expense_data:
			if 'None' in str(combined_expense_data.get(category)):
				combined_expense_data[category] = 0

		return Response(combined_expense_data)
