from django.shortcuts import render, HttpResponseRedirect
from core.forms import StudentRegistration
from core.models import User

def addandshow(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'core/addandshow.html', {'form':fm, 'stu':stud})


def update_data(request, pk):
    if request.method == 'POST':
        pi = User.objects.get(id=pk)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(id=pk)
        fm = StudentRegistration(instance=pi)
    return render(request, 'core/updatestudent.html', {'form':fm})


def delete_data(request, pk):
    if request.method =='POST':
        data = User.objects.get(id=pk)
        data.delete()
        return HttpResponseRedirect('/')

