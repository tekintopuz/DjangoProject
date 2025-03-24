import json
import os.path

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.views import View

from core.settings import BASE_DIR

# Create your views here.
"""
MVC
Model View Controller


MVT
Model-View-Template


View--->Function Based
View--->Class Based
"""

def index(request):
    if request.method == "GET":
        template = loader.get_template('ttw/index.html')
        context = {}
        return HttpResponse(template.render(context, request))


class MyDataClass(View):
    def get(self, request):
        with open(os.path.join(BASE_DIR, "data", "weather.json")) as f:
            my_data = json.load(f)

        return JsonResponse(my_data, safe=False)


class ExchangeClass(View):
    def get(self, request):
        with open(os.path.join(BASE_DIR, "data", "exchange.json")) as f:
            my_data = json.load(f)

        return JsonResponse(my_data, safe=False)
