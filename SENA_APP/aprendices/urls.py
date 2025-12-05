from django.urls import path
from . import views

app_name = 'aprendices'

urlpatterns = [
    path('', views.main, name='main'),
    path('aprendices/', views.aprendices_list, name='lista_aprendices'),
    path('aprendices/crear/', views.AprendizCreateView.as_view(), name='crear_aprendiz'),
    path('aprendices/<str:document>/editar/', views.AprendizUpdateView.as_view(), name='editar_aprendiz'),
    path('aprendices/<str:document>/eliminar/', views.AprendizDeleteView.as_view(), name='eliminar_aprendiz'),
    path('aprendices/<str:document>/', views.aprendices_details, name='aprendices_details'),
]