from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry

        fields = [
                    'title',
                    'body',
                    'img_url'
        ]

        labels = {
                'title'   : 'Titulo Entrada',
                'body'    : 'Cuerpo Entrada',
                'img_url' : 'Link Imagen'
        }

        widgets = {
            'title'   : forms.TextInput(attrs={'class':'form-control','id':'title','placeholder':'Escriba el nombre de su entrada'}),
            'body'    : forms.Textarea(attrs={'class':'form-control','id':'body','placeholder':'Escriba su entrada aqui'}),
            'img_url' : forms.URLInput(attrs={'class':'form-control','id':'img_url','placeholder':'Inserte URL de imagen aqui'})
        }
