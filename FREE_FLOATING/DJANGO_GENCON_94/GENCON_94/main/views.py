from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def start_page(request):
    data = {
        'title': 'Digit Shipping: Smart Contracts'
    }
    return render(request, 'main/start_page.html', data)


def about(request):
    return render(request, 'main/about.html')


def fixing(request):
    return render(request, 'main/fixing.html')


