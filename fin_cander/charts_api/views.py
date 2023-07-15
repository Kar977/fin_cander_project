from rest_framework import generics
from django.shortcuts import render


class GetPeriodData(generics.ListAPIView):
	serializer_class = None
	queryset = None

	def get_queryset(self):
		year = self.kwargs.get("year")
		month = self.kwargs.get("month")
		# TODO zastosowac logike wyszukiwania danych per model nastepnie polaczyc je i zwrocic do queryseta
		pass

# list api znalexc przyklad get api view z get_quesyster