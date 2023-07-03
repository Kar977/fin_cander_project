from django.shortcuts import render, redirect
from finance.forms import IncomeForm, PlanForm, ExpenseForm
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic.list import ListView
from django.views import View
from finance.models import Income


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


class CreateIncomePlanExecuteFirstView(View):
	template_name = "finance/budgeting_start.html"

	def get(self, request, year, month, *args, **kwargs):

		income_form = IncomeForm(year, month, request.POST)
		plan_form = PlanForm(request.POST)
		expense_form = ExpenseForm(year, month, request.POST)
		last_year = year
		last_month = month
		print("Year = ", year)
		print("Month =", month)
		# tu musialbym wsadzic logike, żeby poprawnie odczytywalo dane z DB i przekazywalo do context managera i
		# potem użyć w odpowiednim miejscu w HTML'u
		return render(request, self.template_name, {"income_form": income_form,
													"plan_form": plan_form,
													"expense_form": expense_form,
													"last_year": last_year,
													"last_month": last_month})

	def post(self, request, year, month, *args, **kwargs):
		income_form = IncomeForm(request.POST)
		plan_form = PlanForm(request.POST)
		expense_form = ExpenseForm(request.POST)

		if "income_btn" in request.POST:
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
