
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

def index(request):

    t = get_template('home/index.html')
    html = t.render()
    return HttpResponse(html)