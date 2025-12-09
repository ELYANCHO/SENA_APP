from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Programa
from .forms import ProgramaForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

# VER PROGRAMAS
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def programas(request):
    data = Programa.objects.all().values()
    context = {
        'programas': data,
    }
    return render(request, 'lista_programas.html', context)

def programa_details(request, programa_id):
    programa = Programa.objects.get(id=programa_id)
    context = {
        "programa": programa,
    }
    return render(request, 'programa_detalle.html', context)


# CREATE - PROGRAMA
class ProgramaCreateView(generic.CreateView):
    """Vista para crear un nuevo programa"""
    model = Programa
    form_class = ProgramaForm
    template_name = 'agregar_programa.html'
    success_url = reverse_lazy('programas:lista_programas')
    
    def form_valid(self, form):
        """Mostrar mensaje de exito al crear el programa"""
        messages.success(
            self.request,
            f'El programa {form.instance.nombre} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es invalido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# UPDATE - PROGRAMA
class ProgramaUpdateView(generic.UpdateView):
    """Vista para actualizar un programa existente"""
    model = Programa
    form_class = ProgramaForm
    template_name = 'editar_programa.html'
    success_url = reverse_lazy('programas:lista_programas')
    slug_field = 'id'
    slug_url_kwarg = 'programa_id'
    
    def form_valid(self, form):
        """Mostrar mensaje de exito al actualizar"""
        messages.success(
            self.request,
            f'El programa {form.instance.nombre} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es invalido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# DELETE - PROGRAMA
class ProgramaDeleteView(generic.DeleteView):
    """Vista para eliminar un programa"""
    model = Programa
    template_name = 'eliminar_programa.html'
    success_url = reverse_lazy('programas:lista_programas')
    slug_field = 'id'
    slug_url_kwarg = 'programa_id'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de exito al eliminar"""
        programa = self.get_object()
        messages.success(
            request,
            f'El programa {programa.nombre} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)


