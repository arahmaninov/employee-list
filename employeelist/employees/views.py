from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def employee_list(request):
    return render(request, 'employee_list.html', {
        'employees': Employee.objects.all(),
        'form': EmployeeForm(),
        }) 
