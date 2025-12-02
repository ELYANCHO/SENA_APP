from django.urls import path
from . import views

app_name = 'instructores'

urlpatterns = [
    # list view - mounted under project path 'instructores/'
    path('', views.instructores, name='lista_instructores'),
    # detail view: matches 'instructores/<document>/' when included at project level
    path('<str:document>/', views.instructores_details, name='instructores_details'),
]