from django.urls import path
from . import views

app_name = 'programas'

urlpatterns = [
    path('', views.programas, name='programas'),
    path('<int:programa_id>/', views.detalle_programa, name='programa_detalle'),
]
