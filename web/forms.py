from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio', 'stock', 'destacado', 'descripcion', 'imagen_url']
        labels = {
            'nombre': 'Nombre del producto',
            'categoria': 'Categoría',
            'precio': 'Precio',
            'stock': 'Stock disponible',
            'destacado': 'Mostrar en destacados del inicio',
            'descripcion': 'Descripción',
            'imagen_url': 'URL de imagen',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Radio Motorola DGM8500e VHF'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Radiocomunicación'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '1'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '1'}),
            'destacado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción breve del producto'}),
            'imagen_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
        }