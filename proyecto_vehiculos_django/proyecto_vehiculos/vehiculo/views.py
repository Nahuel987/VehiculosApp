from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm


def index(request):
    return render(request, 'index.html')


def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a la página de inicio u otra página después de guardar
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'agregar_vehiculo.html', {'form': form})


def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'listar_vehiculos.html', {'vehiculos': vehiculos})
