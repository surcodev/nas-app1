from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Gasto(models.Model):
    descripcion = CKEditor5Field('Text', config_name='default')
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    sustento = models.FileField(upload_to='sustentos/')
    fecha = models.DateField()
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    
    class Meta:
            db_table = 'gasto'

    def __str__(self):
        return f"{self.descripcion} - S/ {self.precio}"

