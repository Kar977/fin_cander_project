from django.urls import path
from finance.views.income.crud import FinanceView


urlpatterns = [
	path("fincander/", FinanceView, name="fincander")
]