from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Instructor

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from instructores.forms import InstructorForm
from django.views import generic
from django.contrib import messages
from django.views.generic import FormView


def instructores(request):
    lista_instructores = Instructor.objects.all()
    template = loader.get_template('lista_instructores.html')
    context = {
        'lista_instructores': lista_instructores
    }
    return HttpResponse(template.render(context, request))


def instructores_details(request, document):
    # document corresponds to Instructor.documento_identidad
    instructor = get_object_or_404(Instructor, documento_identidad=document)
    return render(request, 'instructores_details.html', {'instructor': instructor})

class InstructorCreateView(generic.CreateView):
    """Vista para crear un nuevo instructor"""
    model = Instructor
    form_class = InstructorForm
    template_name = 'agregar_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El instructor {form.instance.nombre_completo()} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class InstructorUpdateView(generic.UpdateView):
    """Vista para actualizar un instructor existente"""
    model = Instructor
    form_class = InstructorForm
    template_name = 'editar_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    slug_field = 'documento_identidad'
    slug_url_kwarg = 'document'
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El instructor {form.instance.nombre_completo()} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class InstructorDeleteView(generic.DeleteView):
    """Vista para eliminar un instructor"""
    model = Instructor
    template_name = 'eliminar_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    slug_field = 'documento_identidad'
    slug_url_kwarg = 'document'
    
    def delete(self, request, *args, **kwargs):
        instructor = self.get_object()
        messages.success(
            request,
            f'El instructor {instructor.nombre_completo()} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)