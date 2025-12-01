from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('aprendices/', views.aprendices_list, name='aprendices'),
    path('aprendices/<str:document>/', views.aprendices_details, name='aprendices_details'),
]