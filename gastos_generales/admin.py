from django.contrib import admin
from .models import Gasto

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'categoria', 'precio', 'fecha', 'creado_en')
    list_filter = ('categoria', 'fecha')
    search_fields = ('descripcion', 'categoria')
    date_hierarchy = 'fecha'
    ordering = ('-fecha',)
