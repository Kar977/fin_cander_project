from django.urls import path
from .views import FinanceView


urlpatterns = [
	path("fincander/", FinanceView, name="fincander")
]