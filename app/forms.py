from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, fields, widgets
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from .validators import TamañoMaximoValidator
class ProductoForm(ModelForm):

    nombre = forms.CharField(min_length=5,max_length=20)
    precio = forms.IntegerField(min_value=990)
    descripcion = forms.CharField(min_length=10,max_length=100)
    imagen = forms.ImageField(validators=[TamañoMaximoValidator(maxfile=1)],required=False )

    def clean_nombre(self):
        nom = self.cleaned_data['nombre']
        existe = Producto.objects.filter(nombre__iexact=nom).exists()

        if existe:
            raise ValidationError("este producto ya existe!")
        return nom
    class Meta:
        model = Producto
        fields = ['nombre','precio','descripcion','tipo', 'fecha', 'imagen']

        widgets = {
            'fecha' : forms.SelectDateWidget(years=range(1980,2022))
        }


class CustomUserCreationForm(UserCreationForm):
    pass

