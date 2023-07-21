from django.shortcuts import render
from testapp1.forms import StudentForm

# Create your views here.
def student_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print('Records Inserted into database successfully')
    my_dict = {'form': form}
    return render(request, 'html/form.html', context=my_dict)
