from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Aprendiz

# Create your views here.
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