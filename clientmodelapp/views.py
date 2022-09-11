from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Student

def showstudent(request):
    mystudent = Student.objects.all().values()
    template = loader.get_template('showstudent.html')
    context = {
    'mystudent': mystudent,
    }
    return HttpResponse(template.render(context, request))

def student(request):
    mystudent = Student.objects.all().values()
    output = ""
    for x in mystudent:
        output += x["name"]
    return HttpResponse(output)

def home(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

# Create your views here.
def index(request):
    return HttpResponse("Hello World. This is client Home.")

def add(request):
  template = loader.get_template('addstudent.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['roll']
    y = request.POST['name']
    mystudent = Student(roll=x, name=y)
    mystudent.save()
    return HttpResponseRedirect(reverse('showstudent'))

