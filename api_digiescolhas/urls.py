from django.urls import path
from . import views

urlpatterns = [
    path('', views.DisciplinasDiurnoList.as_view(), name='disciplinasdiurno-list'),

]