from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Instructor


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