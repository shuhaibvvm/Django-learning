from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def print_hello(response):
    movie_details = {
        'title':'Godfather',
        'year':1990,
        'summery':'story of the underworld',
        'success':True
    }
    return render(response,'index.html',movie_details) 