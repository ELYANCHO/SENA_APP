from django import forms
from .models import Programa


class ProgramaForm(forms.ModelForm):
    """Formulario basado en modelo para crear y editar programas"""
    
    class Meta:
        model = Programa
        fields = [
            'codigo',
            'nombre',
            'nivel_formacion',
            'modalidad',
            'duracion_meses',
            'duracion_horas',
            'descripcion',
            'competencias',
            'perfil_egreso',
            'requisitos_ingreso',
            'centro_formacion',
            'regional',
            'estado',
            'fecha_creacion'
        ]
        # Widgets personalizados para mejorar la interfaz en el HTML
        widgets = {
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: ADSO-2025'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del programa'
            }),
            'nivel_formacion': forms.Select(attrs={
                'class': 'form-control'
            }),
            'modalidad': forms.Select(attrs={
                'class': 'form-control'
            }),
            'duracion_meses': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duración en meses'
            }),
            'duracion_horas': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duración en horas'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del programa',
                'rows': 4
            }),
            'competencias': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Competencias a desarrollar',
                'rows': 4
            }),
            'perfil_egreso': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Perfil de egreso',
                'rows': 4
            }),
            'requisitos_ingreso': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Requisitos de ingreso',
                'rows': 4
            }),
            'centro_formacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Centro de formación'
            }),
            'regional': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Regional'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control'
            }),
            'fecha_creacion': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })
        }
        # Etiquetas personalizadas
        labels = {
            'codigo': 'Código del Programa',
            'nombre': 'Nombre',
            'nivel_formacion': 'Nivel de Formación',
            'modalidad': 'Modalidad',
            'duracion_meses': 'Duración (Meses)',
            'duracion_horas': 'Duración (Horas)',
            'descripcion': 'Descripción',
            'competencias': 'Competencias',
            'perfil_egreso': 'Perfil de Egreso',
            'requisitos_ingreso': 'Requisitos de Ingreso',
            'centro_formacion': 'Centro de Formación',
            'regional': 'Regional',
            'estado': 'Estado',
            'fecha_creacion': 'Fecha de Creación'
        }
        
    # Validaciones personalizadas
    
    def clean_codigo(self):
        """Validar que el código no esté vacío"""
        codigo = self.cleaned_data.get('codigo')
        if not codigo or len(codigo.strip()) == 0:
            raise forms.ValidationError("El código del programa no puede estar vacío.")
        return codigo

    def clean_nombre(self):
        """Validar que el nombre tenga longitud mínima"""
        nombre = self.cleaned_data.get('nombre')
        if not nombre or len(nombre.strip()) < 3:
            raise forms.ValidationError("El nombre del programa debe tener al menos 3 caracteres.")
        return nombre

