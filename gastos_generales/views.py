from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required
def lista_gasto(request):
    form = GastoForm()

    if request.method == 'POST':
        form = GastoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gastos_generales:lista_gasto')
        else:
            print("Errores en el formulario:", form.errors)

    gastos_generales = Gasto.objects.all().order_by('-fecha')

    return render(request, 'gastos_generales/home.html', {
        'form': form,
        'gastos_generales': gastos_generales,
    })

@login_required
def eliminar_gasto(request, id):
    registro = get_object_or_404(Gasto, id=id)
    registro.delete()
    return redirect('gastos_generales:lista_gasto')

@login_required
def editar_gasto(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        gasto_general = get_object_or_404(Gasto, id=id)

        form = GastoForm(request.POST, request.FILES, instance=gasto_general)
        if form.is_valid():
            form.save()
            return redirect('gastos_generales:lista_gasto')
        else:
            print(form.errors)
            return redirect('gastos_generales:lista_gasto')

    return redirect('gastos_generales:lista_gasto')