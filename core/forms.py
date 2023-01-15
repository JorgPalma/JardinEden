from django import forms
from .models import Producto, Deposito, Venta

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'


class DepositoForm(forms.ModelForm):
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        to_field_name='nombre',
        required=False,  
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    cantidadp = forms.IntegerField(label="Cantidad de productos", required=False)

    class Meta:
        model = Deposito
        fields = ['producto','cantidadp']

class VentaForm(forms.ModelForm):
    cliente = forms.CharField(label="Nombre del cliente")
    dnicliente = forms.IntegerField(label="DNI cliente")

    class Meta:
        model = Venta
        fields = ['cliente','dnicliente']