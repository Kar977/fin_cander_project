from django import forms
from . import models

from django.core.validators import MinValueValidator, MaxValueValidator

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
	#error_css_class = "error-field"
	#required_css_class = "required-field"
	title_income = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Title"}))

	class Meta:
		model = models.Income
		fields = ["title_income", "amount_income", "date_income"]
		widgets = {"date_income": DateInput()}

"""
	def __int__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields:
			new_data = {
				"placeholder": str(field)
			}
			self.fields[str(field)].widget.attrs.update(new_data)
"""


"""	
	title = forms.CharField(max_length=30)
	amount_income = forms.FloatField(max_value=1000000, min_value=0.1)
	date_income = forms.DateField()
"""


class PlanForm(forms.ModelForm):
	category_plan = forms.ChoiceField(choices=CATEGORY_CHOICES)

	class Meta:
		model = models.Plan
		fields = ["category_plan", "amount_plan"]

	"""
	category_plan = forms.ChoiceField(choices=CATEGORY_CHOICES)
	amount_plan = forms.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(1000000.0)])
	"""


class ExpenseForm(forms.ModelForm):
	category_plan = forms.ChoiceField(choices=CATEGORY_CHOICES)

	class Meta:
		model = models.Expense
		fields = ["category_plan", "amount_expense", "date_expense"]
		widgets = {"date_expense": DateInput()}

	"""
	category_expense = forms.ChoiceField(choices=CATEGORY_CHOICES)
	amount_expense = forms.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(1000000.0)])
	date_expense = forms.DateField(input_formats='%Y-%m-%d')
	"""