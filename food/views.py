from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'food/index.html', context=None)
