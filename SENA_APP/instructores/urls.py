from django.urls import path
from . import views

app_name = 'instructores'

urlpatterns = [
    path('', views.instructores, name='lista_instructores'),
    path('crear/', views.InstructorCreateView.as_view(), name='crear_instructor'),
    path('<str:document>/editar/', views.InstructorUpdateView.as_view(), name='editar_instructor'),
    path('<str:document>/eliminar/', views.InstructorDeleteView.as_view(), name='eliminar_instructor'),
    path('<str:document>/', views.instructores_details, name='instructores_details'),
]