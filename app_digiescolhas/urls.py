from django.contrib import admin
from django.urls import path
from app_digiescolhas.views import DiurnoListView, CursoView

urlpatterns = [
    path('', DiurnoListView.as_view(), name='diurno-list'),
    path('o-curso/', CursoView.as_view(), name='o-curso'),
]