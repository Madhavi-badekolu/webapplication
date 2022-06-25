from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greetings(request):
    print('Hi')
    return HttpResponse('Hello,Welcome to de-haze.com organization.')
