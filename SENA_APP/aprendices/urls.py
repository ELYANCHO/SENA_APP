from django.urls import path
from . import views

app_name = 'aprendices'

urlpatterns = [
    path('', views.main, name='main'),
    path('aprendices/', views.aprendices_list, name='lista_aprendices'),
    path('aprendices/<str:document>/', views.aprendices_details, name='aprendices_details'),
]