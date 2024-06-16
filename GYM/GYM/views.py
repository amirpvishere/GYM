from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def why(request):
    return render(request, "why.html")


