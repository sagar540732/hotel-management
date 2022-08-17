from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return render(request, "app/about.html")

def dashboard(request):
    return render(request, "app/index.html")

def blog(request):
    return render(request, "app/03_index.html")

