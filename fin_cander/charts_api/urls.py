from django.urls import path
from .views import CombinedData, ToalViewData
from django.contrib.auth import views as auth_views

urlpatterns = [

	path("period/<int:year>/<int:month>/", CombinedData.as_view(), name="get_data"),
	path("total/<int:year>/<int:month>/", ToalViewData.as_view(), name="total_view")
]

# /api/income?year=XXX&month=XXX)
