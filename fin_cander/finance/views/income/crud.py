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







"""
	def post(self, request, *args, **kwargs):
		if request.POST.get("income_btn") == "income_btn":
			return redirect("home_site")
		elif request.POST.get("form_type") == "plan_form":
			return redirect("home_site")
		elif request.POST.get("form_type") == "expense_form":
			return redirect("home_site")
		else:
			return HttpResponse("NIC")

"""





"""class BudgetListView(ListView):
	model = Income
	template_name = "finance/create_income.html"
	context_object_name = "incomes"
"""