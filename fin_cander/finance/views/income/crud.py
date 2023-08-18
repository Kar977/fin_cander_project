from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from finance.forms import IncomeForm, PlanForm, ExpenseForm
from finance.models import PeriodTime, Income, Plan, Expense


class CreateIncomePlanExecuteFirstView(LoginRequiredMixin, View):
    template_name = "finance/budgeting_start.html"

    def get(self, request, year, month):
        income_form = IncomeForm(current_year=year, current_month=month)
        plan_form = PlanForm(current_year=year, current_month=month)
        expense_form = ExpenseForm(current_year=year, current_month=month)

        user_data = User.objects.get(username=self.request.user)

        try:
            period_data = PeriodTime.objects.get(year=year, month=month)
        except PeriodTime.DoesNotExist:
            period_data = None

        income_data = Income.objects.filter(user=user_data, date_period=period_data)
        income_total = income_data.aggregate(Sum("amount_income"))["amount_income__sum"]
        plan_data = Plan.objects.filter(user=user_data, date_period=period_data)
        plan_total = plan_data.aggregate(Sum("amount_plan"))["amount_plan__sum"]
        expense_data = Expense.objects.filter(user=user_data, date_period=period_data)
        expense_total = expense_data.aggregate(Sum("amount_expense"))[
            "amount_expense__sum"
        ]

        if income_total is None:
            income_total = 0
        if plan_total is None:
            plan_total = 0
        if expense_total is None:
            expense_total = 0

        final_budget_execution = int(plan_total) - int(expense_total)

        return render(
            request,
            self.template_name,
            {
                "income_form": income_form,
                "plan_form": plan_form,
                "expense_form": expense_form,
                "last_year": year,
                "last_month": month,
                "income_data": income_data,
                "plan_data": plan_data,
                "expense_data": expense_data,
                "income_total": income_total,
                "plan_total": plan_total,
                "expense_total": expense_total,
                "final_budget_execution": final_budget_execution,
            },
        )

    def post(self, request, year, month, *args, **kwargs):
        current_user = User.objects.get(username=self.request.user)
        income_form = IncomeForm(year, month, request.POST)
        plan_form = PlanForm(year, month, request.POST)
        expense_form = ExpenseForm(year, month, request.POST)

        return self.process_request(
            request=request,
            year=year,
            month=month,
            current_user=current_user,
            income_form=income_form,
            plan_form=plan_form,
            expense_form=expense_form,
        )

    def process_request(
        self, request, year, month, current_user, income_form, plan_form, expense_form
    ):
        if "income_btn" in request.POST:
            income = income_form.save(commit=False)
            income.user = current_user
            income.save()
            return redirect("budgeting_first_view", year=year, month=month)
        elif "plan_btn" in request.POST:
            plan = plan_form.save(commit=False)
            plan.user = current_user
            plan.date_plan = datetime.strptime(f"{year}-{month}-01", "%Y-%m-%d").date()
            plan.save()
            return redirect("budgeting_first_view", year=year, month=month)
        elif "expense_btn" in request.POST:
            expense = expense_form.save(commit=False)
            expense.user = current_user
            expense.save()
            return redirect("budgeting_first_view", year=year, month=month)
        else:
            return HttpResponse(
                "Shouldn't happen. \nReport the problem to the IT department"
            )
