from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm
from .models import Alumno
from django.contrib.auth.decorators import login_required

def landing(request):
    return render(request, 'landing.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistroForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def crud_list(request):
    alumnos = Alumno.objects.all()
    return render(request, 'crud_list.html', {'Alumnos': alumnos})
