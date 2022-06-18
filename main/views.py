from django.shortcuts import render
from django.http import HttpResponse
from main.models import Student
from main.forms import StudentForm
from django.shortcuts import redirect

# Create your views here.
def hi(request):
    return HttpResponse('ok guy')

def hello(request):
    return render(request, 'base.html', {})

def home(request):
    students = Student.objects.all()
    return render(request, 'main/home.html', {'students': students})

def create(request):
    # print(request.POST)
    # print(request.method)
    if request.method == "POST":
        student_form = StudentForm(data=request.POST)
        if student_form.is_valid():
            student = student_form.save()
            # print(student)
            return redirect('home')

    form = StudentForm()
    return render(request, 'main/create.html', {'student_form': form})


def update(request, id):
    # print('yes we are in edit file')
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student_form = StudentForm(data=request.POST, instance=student)
        if student_form.is_valid():
            student = student_form.save()
            # print(student)
            return redirect('home')
    form = StudentForm(instance=student)
    return render(request, 'main/update.html', {'student_form': form, 'student': student})

def delete(request, id):
    print(id)
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('home')

def read(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'main/read.html', {'student': student})