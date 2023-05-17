# third parties
from django.shortcuts import render
from django.http import HttpResponse

# local


def index(request):
    return render(request, 'home.html')
