from django.urls import path
#from fin_cander.views.income.crud import FinanceView, AddIncome
from finance.views.income.crud import FinanceView, AddIncome, CreateIncomePlanExecute


urlpatterns = [
	path("fincander/", FinanceView, name="fincander"),
	path("fincander/income", AddIncome, name="add_income"),
	path("fincander/CRUD", CreateIncomePlanExecute.as_view(), name="crud")
]