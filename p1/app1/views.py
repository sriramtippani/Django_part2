import random

from django.shortcuts import render
from datetime import *
from random import *

# Create your views here.
def create_view(request):
    message_1 = [
        'The Golden days ahead',
        'Better to sleep more time even in office',
        'Tomorrow will be the best day of your life',
        'tomorrow is the perfect day to propose your girl friend',
        'Very soon you will get Job'
    ]
    name_list = ['sunny', 'Mallika', 'Katrina', 'Kareena', 'Samantha', 'Priyanka']
    time_1 = datetime.now()
    h_t = int(time_1.strftime('%H'))
    if h_t < 12:
        s = 'Good Morning'
    elif h_t < 16:
        s = 'Good Afternoon'
    elif h_t < 21:
        s = 'Good Evening'
    else:
        s = 'Good Night'

    name = choice(name_list)
    message = choice(message_1)
    m_Dict = {'Time': time_1, 'Name': name, 'Message': message, 'Wish': s}
    return render(request, 'test1/a1.html', context= m_Dict)