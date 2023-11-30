from django.shortcuts import render
from .models import Employee

# Create your views here.
def index(request):
    return render(request, "index.html")

def employee_list(request):
    return render(request, 'employee_list.html', {'employees': Employee.objects.all()} ) 
