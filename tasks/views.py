from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # Work With database
    # Transform Data
    # data pass
    # Http response / Json response
    return HttpResponse("<h1>Welcome Task Management System</h1>")
def contact(request):
    return HttpResponse("<strong style='color:red;'>This is Contact Page<strong>")
def show_task(request):
    return HttpResponse("Show Your Task")
def show_specific_task(request,id):
    print("id",id)
    print("id type", type(id))
    return HttpResponse("This is Specific task page")
def dashbord(request,id):
    return HttpResponse("This Dashbord Page")