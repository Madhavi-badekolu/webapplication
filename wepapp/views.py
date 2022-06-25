from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greetings(request):
    print('Hi')
    return HttpResponse('Helllooo,Welcome to de-haze.com organization, Nice to have you here.')