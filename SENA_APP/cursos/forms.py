from django import forms
from .models import Curso


class CursoForm(forms.ModelForm):
    """Formulario basado en modelo para crear y editar cursos"""
    
    class Meta:
        model = Curso
        fields = [
            'codigo',
            'nombre',
            'programa',
            'instructor_coordinador',
            'fecha_inicio',
            'fecha_fin',
            'horario',
            'aula',
            'cupos_maximos',
            'estado',
            'observaciones'
        ]
        # Widgets personalizados para mejorar la interfaz en el HTML
        widgets = {
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: ADSO-2025-001'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del curso'
            }),
            'programa': forms.Select(attrs={
                'class': 'form-control'
            }),
            'instructor_coordinador': forms.Select(attrs={
                'class': 'form-control'
            }),
            'fecha_inicio': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'fecha_fin': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'horario': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Lunes a Viernes 8:00 AM - 5:00 PM'
            }),
            'aula': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Aula o ambiente'
            }),
            'cupos_maximos': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número máximo de aprendices'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Observaciones adicionales',
                'rows': 4
            })
        }
        # Etiquetas personalizadas
        labels = {
            'codigo': 'Código del Curso',
            'nombre': 'Nombre',
            'programa': 'Programa de Formación',
            'instructor_coordinador': 'Instructor Coordinador',
            'fecha_inicio': 'Fecha de Inicio',
            'fecha_fin': 'Fecha de Finalización',
            'horario': 'Horario',
            'aula': 'Aula/Ambiente',
            'cupos_maximos': 'Cupos Máximos',
            'estado': 'Estado',
            'observaciones': 'Observaciones'
        }
        
    # Validaciones personalizadas
    
    def clean_codigo(self):
        """Validar que el código no esté vacío"""
        codigo = self.cleaned_data.get('codigo')
        if not codigo or len(codigo.strip()) == 0:
            raise forms.ValidationError("El código del curso no puede estar vacío.")
        return codigo

    def clean_nombre(self):
        """Validar que el nombre tenga longitud mínima"""
        nombre = self.cleaned_data.get('nombre')
        if not nombre or len(nombre.strip()) < 3:
            raise forms.ValidationError("El nombre del curso debe tener al menos 3 caracteres.")
        return nombre
