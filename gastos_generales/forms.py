from django import forms
from .models import Gasto
from tinymce.widgets import TinyMCE

class GastoForm(forms.ModelForm):
    descripcion = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 10}))
    class Meta:
        model = Gasto
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name != 'descripcion':
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['autocomplete'] = 'off'
