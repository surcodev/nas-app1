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