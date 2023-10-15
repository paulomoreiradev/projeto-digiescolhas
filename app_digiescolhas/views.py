from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import DisciplinasDiurno
# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"


class CursoView(TemplateView):
    template_name = "o-curso.html"


class DiurnoListView (ListView):
    model = DisciplinasDiurno
    template_name = "disciplinasdiurno_list.html"