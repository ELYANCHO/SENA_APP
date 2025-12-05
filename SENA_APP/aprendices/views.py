from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Aprendiz

from .forms import AprendizForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

# VER APRENDICES
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def aprendices_list(request):
  data = Aprendiz.objects.all().values()
  context = {
    'aprendices':data,
  }
  return render(request, 'aprendices_list.html', context)

def aprendices_details(request, document):
    aprendiz = Aprendiz.objects.get(document=document)
    context = {
        "aprendiz": aprendiz,
    }
    return render(request, 'aprendices_details.html', context)


# CREATE - APRENDIZ

class AprendizCreateView(generic.CreateView):
    """Vista para crear un nuevo aprendiz"""
    model = Aprendiz
    form_class = AprendizForm
    template_name = 'agregar_aprendiz.html'
    success_url = reverse_lazy('aprendices:lista_aprendices')
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el aprendiz"""
        messages.success(
            self.request,
            f'El aprendiz {form.instance.nombre()} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# UPDATE - APRENDIZ
class AprendizUpdateView(generic.UpdateView):
    """Vista para actualizar un aprendiz existente"""
    model = Aprendiz
    form_class = AprendizForm
    template_name = 'editar_aprendiz.html'
    success_url = reverse_lazy('aprendices:lista_aprendices')
    slug_field = 'document'
    slug_url_kwarg = 'document'
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar"""
        messages.success(
            self.request,
            f'El aprendiz {form.instance.nombre()} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# DELETE - APRENDIZ
class AprendizDeleteView(generic.DeleteView):
    """Vista para eliminar un aprendiz"""
    model = Aprendiz
    template_name = 'eliminar_aprendiz.html'
    success_url = reverse_lazy('aprendices:lista_aprendices')
    slug_field = 'document'
    slug_url_kwarg = 'document'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar"""
        aprendiz = self.get_object()
        messages.success(
            request,
            f'El aprendiz {aprendiz.nombre()} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)