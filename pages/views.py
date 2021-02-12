from django.shortcuts import render
from django.http import HttpResponse
import logging


# Create your views here.

def home_view(request, *args, **kwargs):
    # logging.basicConfig(level=logging.DEBUG)
    # logging.debug(request.user)

    # return HttpResponse('<h1> Hello world</h1>')
    my_context = {
        'name': 'Venkat Shrikrishna',
        'roll_num': 20,
        'std': 4,
        'friends': ["A", "B", "C"]
    }
    return render(request, 'home.html', my_context)
