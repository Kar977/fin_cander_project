from django.urls import path, register_converter
#from fin_cander.views.income.crud import FinanceView, AddIncome
from finance.views.income.crud import CreateIncomePlanExecuteFirstView
from finance.converters import DateConverter

register_converter(DateConverter, "date")

urlpatterns = [
	path("chose/<int:year>/<int:month>/", CreateIncomePlanExecuteFirstView.as_view(), name="budgeting_first_view"),
]