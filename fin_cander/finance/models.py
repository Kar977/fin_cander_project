from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.utils import timezone


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


class Income(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date_period = models.ForeignKey(PeriodTime, on_delete=models.CASCADE)
	title_income = models.CharField(max_length=30)
	amount_income = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(1000000.0)])
	date_income = models.DateField(default=timezone.now())


class Plan(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date_period = models.ForeignKey(PeriodTime, on_delete=models.CASCADE, default=timezone.now())
	category_plan = models.CharField(choices=CATEGORY_CHOICES)
	amount_plan = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(1000000.0)])
	date_plan = models.DateField(default=timezone.now())


class Expense(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date_period = models.ForeignKey(PeriodTime, on_delete=models.CASCADE, default=timezone.now())
	category_plan = models.CharField(choices=CATEGORY_CHOICES)
	amount_expense = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(1000000.0)])
	date_expense = models.DateField(default=timezone.now())
