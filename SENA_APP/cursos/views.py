from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Curso
from .forms import CursoForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

# VER CURSOS
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def cursos(request):
    data = Curso.objects.all().values()
    context = {
        'cursos': data,
    }
    return render(request, 'lista_cursos.html', context)

def curso_details(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    aprendices_curso = curso.aprendizcurso_set.all()
    instructores_curso = curso.instructorcurso_set.all()
    context = {
        "curso": curso,
        "aprendices_curso": aprendices_curso,
        "instructores_curso": instructores_curso,
    }
    return render(request, 'detalle_curso.html', context)


# CREATE - CURSO
class CursoCreateView(generic.CreateView):
    """Vista para crear un nuevo curso"""
    model = Curso
    form_class = CursoForm
    template_name = 'agregar_curso.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    
    def form_valid(self, form):
        """Mostrar mensaje de exito al crear el curso"""
        messages.success(
            self.request,
            f'El curso {form.instance.nombre} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es invalido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# UPDATE - CURSO
class CursoUpdateView(generic.UpdateView):
    """Vista para actualizar un curso existente"""
    model = Curso
    form_class = CursoForm
    template_name = 'editar_curso.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    slug_field = 'id'
    slug_url_kwarg = 'curso_id'
    
    def form_valid(self, form):
        """Mostrar mensaje de exito al actualizar"""
        messages.success(
            self.request,
            f'El curso {form.instance.nombre} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es invalido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# DELETE - CURSO
class CursoDeleteView(generic.DeleteView):
    """Vista para eliminar un curso"""
    model = Curso
    template_name = 'eliminar_curso.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    slug_field = 'id'
    slug_url_kwarg = 'curso_id'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de exito al eliminar"""
        curso = self.get_object()
        messages.success(
            request,
            f'El curso {curso.nombre} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)