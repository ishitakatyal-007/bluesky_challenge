from django.shortcuts import render

# Create your views here.
from datetime import date

from rest_framework.views import APIView
from django.http import HttpResponse

from categories.models import EmissionCategories
from countries.models import Countries
from .models import GHGsEmissions
from .serializers import EmissionSerializer

current_year = date.today().year

def fetch_country_data(country, start_year, end_year, categories):
    if start_year is None:
        start_year = 1990
    if end_year is None:
        end_year = 2014
    if categories is None:
        categories = EmissionCategories.objects.all().values("category_alias")
    else:
        categories = [i for i in categories.split(",")]
           
    country_data = {}
    country_list = []
    for category in categories:
        if type(category) is dict:
            alias = category["category_alias"]
        else:
            alias = category
        category_dict = {}
        data = GHGsEmissions.objects.filter(country_id=country, year__range=[start_year, end_year], category_id=EmissionCategories.objects.filter(category_alias=alias).first()).values("year", "value").all()

        category_dict[alias] = [i for i in data]
        country_list.append(category_dict)
    
    country = str(country).split("--")[1]
    country_data[country] = country_list
    return country_data

class EmissionView(APIView):
    ser_class = EmissionSerializer

    def get(self, request):
        country_list = Countries.objects.all()
        year_dict = {}
        for country in country_list:
            country_id, country_name = str(country).split("--")
            if country_id is not None:
                ghg_emission_records = GHGsEmissions.objects.filter(country_id=country_id).distinct("year").values("year").all()

                if len(ghg_emission_records) != 0:
                    year_list = []
                    for emission_record in ghg_emission_records:
                        year_list.append(emission_record["year"])
                    year_dict[country_name] = {"start_year": min(year_list), "max_year": max(year_list)}
        
        return HttpResponse(str(year_dict))
        
class TemporalEmissions(APIView):
    ser_class = EmissionSerializer

    def get(self, request, country_id, start_year, end_year):
        
        print(country_id)
        
        if country_id is None:
            return HttpResponse("Country ID cannot be None... :(")
        if start_year <= 0: 
            x = "Start year cannot be 0 or negative... :(" + str(start_year)
            return HttpResponse(x)
        if end_year <= 0: 
            x = "End year cannot be 0 or negative... :("
            return HttpResponse(x)
        if start_year > current_year:
            x = "Start year cannot be in future.. :(" + str(start_year)
            return HttpResponse(x)
        if end_year > current_year:
            x = "End year cannot be in furture.. :(" + str(end_year)
            return HttpResponse(x)
        if start_year > end_year:
            x = "Start year: " + str(start_year) + " cannot be greater than end year: " + str(end_year)
            return HttpResponse(x)


        country_name = Countries.objects.filter(country_id=country_id).first()

        if start_year == end_year:
           x = str(fetch_country_data(country_name, start_year, end_year, None))
           return HttpResponse(x) 

        if start_year is None:
            start_year = 1990
        if end_year is None:
            end_year = 2014

        x = str(fetch_country_data(country_name, start_year, end_year, None))
        return HttpResponse(x)

class CategoricalEmissions(APIView):
    ser_class = EmissionSerializer

    def get(self, request, country_id, categories):
        country_name = Countries.objects.filter(country_id=country_id).first()
        x = str(fetch_country_data(country_name, None, None, categories))
        return HttpResponse(x)

class ParametricEmissions(APIView):
    ser_class = EmissionSerializer

    def get(self, request, country_id, start_year, end_year, categories):
        country_name = Countries.objects.filter(country_id=country_id).first()
        x = str(fetch_country_data(country_name, start_year, end_year, categories))
        return HttpResponse(x)
