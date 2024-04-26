from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def print_hello(response):
    movies_data ={'movie' :[
    {
        'title': 'Godfather',
        'year': 1990,
        'summary': 'Story of the underworld',
        'success': True
    },
    {
        'title': 'The Shawshank Redemption',
        'year': 1994,
        'summary': 'A story of hope and friendship in prison',
        'success': True
    },
    {
        'title': 'Inception',
        'year': 2010,
        'summary': 'A mind-bending journey through dreams',
        'success': True
    },
    {
        'title': 'Pulp Fiction',
        'year': 1994,
        'summary': 'A series of interconnected stories about crime and redemption',
        'success': True
    },
    {
        'title': 'The Dark Knight',
        'year': 2008,
        'summary': 'A tale of Batman facing the Joker in Gotham',
        'success': True
    },
    {
        'title': 'Battlefield Earth',
        'year': 2000,
        'summary': 'An alien race enslaves humanity in the year 3000',
        'success': False
    },
    {
        'title': 'Cats',
        'year': 2019,
        'summary': 'A group of cats compete in a singing and dancing competition',
        'success': False
    },
    {
        'title': 'The Last Airbender',
        'year': 2010,
        'summary': 'A boy with elemental powers embarks on a quest to save the world',
        'success': False
    }
]}

    return render(response,'index.html',movies_data) 