from django.shortcuts import render

# Create your views here.
def f1(request):
    return render(request, 'template1/index.html')

def sports_view(request):
    h1 = 'Playing sports teaches lessons of life, such as teamwork, accountability, self-confidence, responsibility, and self-discipline.'
    m1 = 'shuttle'
    m2 = 'criket'
    m3 = 'foodball'
    type = 'sports'
    m_dir = {'h1': h1, 'm1': m1, 'm2': m2, 'm3': m3, 'type': type}
    return render(request, 'template1/page.html', context=m_dir)

def movies_view(request):
    h1 = 'Enjoy the Digits hq cinema experience.'
    m1 = 'cinema1'
    m2 = 'cinema2'
    m3 = 'cinema3'
    type = 'movies'
    m_dir1 = {'h1': h1, 'm1': m1, 'm2': m2, 'm3': m3, 'type': type}
    return render(request, 'template1/page.html', context=m_dir1)

def politics_view(request):
    h1 = 'Politics life is very crucial.'
    m1 = 'politician1'
    m2 = 'politician2'
    m3 = 'politician3'
    type = 'politics'
    m_dir2 = {'h1': h1, 'm1': m1, 'm2': m2, 'm3': m3, 'type': type}
    return render(request, 'template1/page.html', context=m_dir2)
