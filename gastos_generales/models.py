from django.db import models

class Gasto(models.Model):
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    soles = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dolares = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sustento = models.FileField(upload_to='files/gastos_generales/', blank=True, null=True)
    fecha = models.DateField()
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    
    class Meta:
            db_table = 'gasto'

    def __str__(self):
        return f"{self.descripcion}"

