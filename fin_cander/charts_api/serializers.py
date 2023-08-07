from rest_framework import serializers
from finance.models import PeriodTime, Income, Plan, Expense, User


class PeriodTimeSerializer(serializers.ModelSerializer):
	class Meta:
		model = PeriodTime
		fields = '__all__'


class IncomeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Income
		fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
	class Meta:
		model = Plan
		fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Expense
		fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'
