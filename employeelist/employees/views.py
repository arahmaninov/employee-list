from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def employee_list(request):
    context = {}
    employees = Employee.objects.all()
    context['employees'] = employees
    form = EmployeeForm()

    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = EmployeeForm(request.POST)
            else:
                employee = Employee.objects.get(id=pk)
                form = EmployeeForm(request.POST, instance=employee)
            form.save()
            form = EmployeeForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            employee = Employee.objects.get(id=pk)
            employee.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            employee = Employee.objects.get(id=pk)
            form = EmployeeForm(instance=employee)

    context['form'] = form

    return render(request, 'employee_list.html', context) 
