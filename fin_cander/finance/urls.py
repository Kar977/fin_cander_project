from django.urls import path, register_converter

from finance.converters import DateConverter
from finance.views.income.crud import CreateIncomePlanExecuteFirstView

register_converter(DateConverter, "date")

urlpatterns = [
    path(
        "chose/<int:year>/<int:month>/",
        CreateIncomePlanExecuteFirstView.as_view(),
        name="budgeting_first_view",
    ),
]
