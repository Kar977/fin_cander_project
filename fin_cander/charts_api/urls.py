from django.urls import path

from charts_api.views import (
    CombinedData,
    TotalViewData,
    DetailedPlanViewData,
    DetailedExpenseViewData,
    DeletePlan,
    DeleteExpense,
    DeleteIncome,
)

urlpatterns = [
    path("period/<int:year>/<int:month>/", CombinedData.as_view(), name="get_data"),
    path("total/<int:year>/<int:month>/", TotalViewData.as_view(), name="total_view"),
    path(
        "plan/<int:year>/<int:month>/", DetailedPlanViewData.as_view(), name="plan_view"
    ),
    path(
        "expense/<int:year>/<int:month>/",
        DetailedExpenseViewData.as_view(),
        name="expense_view",
    ),
    path("delete-plan/<int:plan_id>/", DeletePlan.as_view(), name="delete_plan"),
    path(
        "delete-income/<int:income_id>/", DeleteIncome.as_view(), name="delete-income"
    ),
    path(
        "delete-expense/<int:expense_id>/",
        DeleteExpense.as_view(),
        name="delete-expense",
    ),
]
