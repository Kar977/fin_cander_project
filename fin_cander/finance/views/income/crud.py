from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def FinanceView(request):
	return render(request, "finance/base.html")