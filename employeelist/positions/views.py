from django.shortcuts import render

from .models import Position
from .forms import PositionForm

# Create your views here.
def positionlist(request):
    context = {}
    positions = Position.objects.all()
    context['positions'] = positions
    form = PositionForm()

    if request.method == 'POST':
        if 'add' in request.POST:
            pk = request.POST.get('add')
            if not pk:
                form = PositionForm(request.POST)
            else:
                position = Position.objects.get(id=pk)
                form = PositionForm(request.POST, instance=position)
            form.save()
            form = PositionForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            position = Position.objects.get(id=pk)
            position.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            position = Position.objects.get(id=pk)
            form = PositionForm(instance=position)

    context['form'] = form

    return render(request, 'position_list.html', context)
