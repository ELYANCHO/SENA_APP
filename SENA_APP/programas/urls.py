from django.urls import path
from . import views

app_name = 'programas'

urlpatterns = [
    path('', views.programas, name='lista_programas'),
    path('crear/', views.ProgramaCreateView.as_view(), name='crear_programa'),
    path('<int:programa_id>/editar/', views.ProgramaUpdateView.as_view(), name='editar_programa'),
    path('<int:programa_id>/eliminar/', views.ProgramaDeleteView.as_view(), name='eliminar_programa'),
    path('<int:programa_id>/', views.programa_details, name='programa_detalle'),
]
