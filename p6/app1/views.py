from django.shortcuts import render
from app1.forms import FeedBackForm

# Create your views here.
def feedback_view(request):
    form = FeedBackForm()
    set = False
    name = ''
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print('Form validation success and printing feedback information.')
            print('#' * 30)
            print('Name: ', form.cleaned_data['name'])
            print('RollNo: ', form.cleaned_data['rollno'])
            print('MailId: ', form.cleaned_data['email'])
            print('Feedback: ', form.cleaned_data['feedback'])
            set = True
            name = form.cleaned_data['name']

    my_dict = {'form': form, 'set': set, 'name': name}
    return render(request, 'html/feedback.html', context=my_dict)
