from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

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
    template = loader.get_template('ttw/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

