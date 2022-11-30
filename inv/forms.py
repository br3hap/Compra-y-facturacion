from django import forms

from .models import Categoria, SubCategoria, Marca

class CategoriaForm(forms.ModelForm):
    class Meta:
        model =  Categoria
        fields = ['descripcion','estado']
        labels = {'descripcion':'Descripcion de la Categoria',
                    'estado':'Estado'}
        widget = {'descripcion':forms.TextInput}

    def __init__(self,*args, **Kwargs):
        super().__init__(*args, **Kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset = Categoria.objects.filter(estado=True).order_by('descripcion')
    )
    class Meta:
        model =  SubCategoria
        fields = ['categoria','descripcion','estado']
        labels = {'descripcion':'Sub Categoria',
                    'estado':'Estado'}
        widget = {'descripcion':forms.TextInput}

    def __init__(self,*args, **Kwargs):
        super().__init__(*args, **Kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['categoria'].empty_label = 'Seleccione Categoria'

class MarcaForm(forms.ModelForm):
    class Meta:
        model =  Marca
        fields = ['descripcion','estado']
        labels = {'descripcion':'Descripcion de la Marca',
                    'estado':'Estado'}
        widget = {'descripcion':forms.TextInput}

    def __init__(self,*args, **Kwargs):
        super().__init__(*args, **Kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })