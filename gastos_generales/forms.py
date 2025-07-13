from django import forms
from .models import Gasto

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # Evitar interferencias en el editor CKEditor
            if name != 'descripcion':
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['autocomplete'] = 'off'
