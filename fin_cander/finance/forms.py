from django import forms
from . import models


CATEGORY_CHOICES = [
	("", "Select a category"),
	("Debt Payments", "Debt Payments"),
	("Investing", "Investing"),
	("Saving", "Saving"),
	("Housing", "Housing"),
	("Food", "Food"),
	("Utilities", "Utilities"),
	("Medical & Healthcare", "Medical & Healthcare"),
	("Personal Spending", "Personal Spending"),
	("Recreation & Entertainment", "Recreation & Entertainment"),
	("Miscellaneous", "Miscellaneous")
]


class DateInput(forms.DateInput):
	input_type = "date"


class IncomeForm(forms.ModelForm):
	title_income = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Title"}))

	def __init__(self, current_year, current_month, *args, **kwargs):
		super().__init__(*args, **kwargs)

		min_date = f"{current_year}-0{current_month}-01"
		max_date = f"{current_year}-0{current_month}-20"
		print("max", max_date)
		print("min", min_date)

		self.fields["date_income"].widget.attrs.update({"min": min_date, "max": max_date})

	class Meta:
		model = models.Income
		fields = ["title_income", "amount_income", "date_income"]
		widgets = {"date_income": DateInput()}


class PlanForm(forms.ModelForm):
	category_plan = forms.ChoiceField(choices=CATEGORY_CHOICES)

	class Meta:
		model = models.Plan
		fields = ["category_plan", "amount_plan"]


class ExpenseForm(forms.ModelForm):
	category_plan = forms.ChoiceField(choices=CATEGORY_CHOICES)

	class Meta:
		model = models.Expense
		fields = ["category_plan", "amount_expense", "date_expense"]
		widgets = {"date_expense": DateInput()}
