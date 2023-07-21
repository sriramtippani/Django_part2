from django.shortcuts import render


# Create your views here.
def m1(request):
    my_dict = {'head_msg': 'Movies Information',
                'sub_msg1': 'Sonali slowly getting cured',
                'sub_msg2': 'Bahubali-3 is just planning',
                'sub_msg3': 'Salman Khan ready to marriage'}
    return render(request, 'testApp/index.html', context=my_dict)

def m2(request):
    my_dict = {'head_msg': 'Sports Information',
               'sub_msg1': 'Anushka Sharma Firing Like anything',
               'sub_msg2': 'Kohli updating in game anything can happend',
               'sub_msg3': 'Worst Performance by India-Sehwag'}
    return render(request, 'testApp/index.html', context=my_dict)

def m3(request):
    my_dict = {'head_msg': 'Politics Information',
               'sub_msg1': 'Achhce Din Aaa gaya',
               'sub_msg2': 'Rupee Value now 1$:70Rs',
               'sub_msg3': 'In India Single Paisa Black money No more'}
    return render(request, 'testApp/index.html', context=my_dict)

def m4(request):
    return render(request, 'testApp/demo.html')

