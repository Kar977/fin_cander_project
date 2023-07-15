from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.utils import timezone
from django.conf import settings


CATEGORY_CHOICES = (
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
)


class PeriodTime(models.Model):
	year = models.IntegerField(default=timezone.now().year)
	month = models.IntegerField(default=timezone.now().month)

	def __str__(self):
		return f"{self.year}/{self.month}"


class Income(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date_period = models.ForeignKey(PeriodTime, on_delete=models.CASCADE)
	title_income = models.CharField(max_length=30)
	amount_income = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(1000000.0)])
	date_income = models.DateField(default=timezone.now())

	def __str__(self):
		return f"Income: {self.title_income}/{self.date_income}/{self.user}"

	def save(self, *args, **kwargs):

		# TODO implement logic for filling out the date_period field
		selected_year = self.date_income.year
		selected_month = self.date_income.month

		period_of_time, created = PeriodTime.objects.get_or_create(year=selected_year, month=selected_month)
		self.date_period = period_of_time

		super(Income, self).save(*args, **kwargs)


class Plan(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date_period = models.ForeignKey(PeriodTime, on_delete=models.CASCADE, default=timezone.now())
	category_plan = models.CharField(choices=CATEGORY_CHOICES)
	amount_plan = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(1000000.0)])
	date_plan = models.DateField(default=timezone.now())

	def __str__(self):
		return f"Plan: {self.category_plan}/{self.date_plan}/{self.user}"

	def save(self, *args, **kwargs):
		selected_year = self.date_plan.year
		selected_month = self.date_plan.month

		period_of_time, created = PeriodTime.objects.get_or_create(year=selected_year, month=selected_month)
		self.date_period = period_of_time

		super(Plan, self).save(*args, **kwargs)


class Expense(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date_period = models.ForeignKey(PeriodTime, on_delete=models.CASCADE, default=timezone.now())
	category_plan = models.CharField(choices=CATEGORY_CHOICES)
	amount_expense = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(1000000.0)])
	date_expense = models.DateField(default=timezone.now())

	def __str__(self):
		return f"Expense: {self.category_plan}/{self.date_expense}/{self.user}"

	def save(self, *args, **kwargs):

		# TODO implement logic for filling out the date_period field
		selected_year = self.date_expense.year
		selected_month = self.date_expense.month

		period_of_time, created = PeriodTime.objects.get_or_create(year=selected_year, month=selected_month)
		self.date_period = period_of_time

		super(Expense, self).save(*args, **kwargs)
