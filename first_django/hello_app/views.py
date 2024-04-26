from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def print_hello(response):
    return HttpResponse("<b>Hello world<b>")