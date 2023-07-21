from django.shortcuts import render
from django.http import HttpResponse
from datetime import *

# Create your views here.
def td(request):
    t1 = datetime.now()
    h = int(t1.strftime('%H'))
    msg = '<h1> Hello Friend, '
    if h < 12:
        msg = msg + 'Good Morning'
    elif h < 16:
        msg = msg + 'Good Afternoon'
    elif h < 21:
        msg = msg + 'Good Evening'
    else:
        msg = msg + 'Good Night'
    msg = msg + '</h1><hr>'
    msg = msg + '<h1>Now server Date and Time: ' + str(t1) + '</h1>'
    print(msg)
    return HttpResponse(msg)
