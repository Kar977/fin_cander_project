from django.urls import path, register_converter
#from fin_cander.views.income.crud import FinanceView, AddIncome
from finance.views.income.crud import FinanceView, AddIncome, CreateIncomePlanExecute, CreateIncomePlanExecuteFirstView
from finance.converters import DateConverter

register_converter(DateConverter, "date")

urlpatterns = [
	path("fincander/", FinanceView, name="fincander"),
	path("fincander/income", AddIncome, name="add_income"),
	path("fincander/CRUD", CreateIncomePlanExecute.as_view(), name="crud"),
	path("chose/<int:year>/<int:month>/", CreateIncomePlanExecuteFirstView.as_view(), name="budgeting_first_view"),
	path("chose/<int:year>/<int:month>/", CreateIncomePlanExecute.as_view(), name="crud2")
]