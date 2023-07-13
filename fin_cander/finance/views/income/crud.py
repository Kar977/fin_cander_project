from django.shortcuts import render, redirect
from finance.forms import IncomeForm, PlanForm, ExpenseForm
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic.list import ListView
from django.views import View
from finance.models import Income
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from datetime import datetime


# Create your views here.
def FinanceView(request):
	return render(request, "finance/base.html")


def AddIncome(request):
	if request.method == "POST":
		form = IncomeForm(request.POST)
		if form.is_valid():
			title_of_income = form.cleaned_data.get('title')
			messages.success(request, f"Succes of submit clik for {title_of_income}!")
			return redirect("home_site")
	else:
		form = IncomeForm()

	return render(request, "finance/create_income.html", {"form": form})


class CreateIncomePlanExecute(View):
	template_name = "finance/create_income.html"

	def get(self, request, *args, **kwargs):

		income_form = IncomeForm(request.POST)
		plan_form = PlanForm(request.POST)
		expense_form = ExpenseForm(request.POST)

		return render(request, self.template_name, {"income_form": income_form, "plan_form": plan_form, "expense_form": expense_form})

	def post(self, request, *args, **kwargs):
		income_form = IncomeForm(request.POST)
		plan_form = PlanForm(request.POST)
		expense_form = ExpenseForm(request.POST)

		if "income_btn" in request.POST:
			if income_form.is_valid():
				income_form.save()
			return HttpResponse("INCOME ADDED")
		elif "plan_btn" in request.POST:
			plan_form.save()
			return HttpResponse("PLAN ADDED")
		elif "expense_btn" in request.POST:
			expense_form.save()
			return HttpResponse("EXPENSE ADDED")
		else:
			return HttpResponse("Nothing")


class CreateIncomePlanExecuteFirstView(LoginRequiredMixin, View):
	template_name = "finance/budgeting_start.html"

	def get(self, request, year, month):
		income_form = IncomeForm(current_year=year, current_month=month)
		plan_form = PlanForm(current_year=year, current_month=month)
		expense_form = ExpenseForm(current_year=year, current_month=month)

		print("Year = ", year)
		print("Month =", month)
		# tu musialbym wsadzic logike, żeby poprawnie odczytywalo dane z DB i przekazywalo do context managera i
		# potem użyć w odpowiednim miejscu w HTML'u
		return render(request, self.template_name, {"income_form": income_form,
													"plan_form": plan_form,
													"expense_form": expense_form,
													"last_year": year,
													"last_month": month})

	def post(self, request, year, month, *args, **kwargs):
		print(year, month)
		current_user = User.objects.get(username=self.request.user)
		income_form = IncomeForm(year, month, request.POST)
		plan_form = PlanForm(year, month, request.POST)
		expense_form = ExpenseForm(year, month, request.POST)

		if "income_btn" in request.POST:
			income = income_form.save(commit=False)
			income.user = current_user
			income.save()
			return HttpResponse("INCOME ADDED")
		elif "plan_btn" in request.POST:
			plan = plan_form.save(commit=False)
			plan.user = current_user
			plan.date_plan = datetime.strptime(f"{year}-{month}-01", "%Y-%m-%d").date()
			plan.save()
			return HttpResponse("PLAN ADDED")
		elif "expense_btn" in request.POST:
			expense = expense_form.save(commit=False)
			expense.user = current_user
			expense.save()
			return HttpResponse("EXPENSE ADDED")
		else:
			return HttpResponse("Nothing")
