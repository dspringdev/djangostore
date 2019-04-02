from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# /products -> index
def index(request):
    return HttpResponse('Hello World')


def new(request):
    return HttpResponse('New Products')


def offer(request):
    return HttpResponse('Offer')
