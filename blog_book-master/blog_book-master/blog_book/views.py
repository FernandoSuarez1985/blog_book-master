from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    my_context = {}
    return render(request, "index.html", context = my_context)


def my_base(request):
    my_context = {}
    return render(request, "base.html", context = my_context)


def my_view(request):
    return HttpResponse("View")
