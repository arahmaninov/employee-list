from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def employee_list(request):
    context = {}
    employees = Employee.objects.all()
    form = EmployeeForm()
    context['employees'] = employees
    context['form'] = form

    if request.method == 'POST':
        if 'save' in request.POST:
            form = EmployeeForm(request.POST)
            form.save()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            employee = Employee.objects.get(id=pk)
            employee.delete()

    context['form'] = form

    return render(request, 'employee_list.html', context) 
