from django import forms
from .models import Gasto
from tinymce.widgets import TinyMCE  # ✅ Usa el widget de TinyMCE

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = '__all__'
        widgets = {
            'descripcion': TinyMCE(attrs={'cols': 80, 'rows': 10}),
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['autocomplete'] = 'off'
