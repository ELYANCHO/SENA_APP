from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Curso
from django.http import HttpResponse

# Create your views here.
def lista_cursos(request):
    cursos = Curso.objects.all()
    context = {
        'lista_cursos': cursos,
        'total_cursos': cursos.count(),
    }
    return render(request, 'lista_cursos.html', context)

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    aprendices_curso = curso.aprendizcurso_set.all()
    instructores_curso = curso.instructorcurso_set.all()
    
    context = {
        'curso': curso,
        'aprendices_curso': aprendices_curso,
        'instructores_curso': instructores_curso,
    }
    
    return render(request, 'detalle_curso.html', context)