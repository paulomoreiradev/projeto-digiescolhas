from django.shortcuts import render
from rest_framework import generics
from app_digiescolhas.models import DisciplinasDiurno
from .serializers import DisciplinasDiurnoSerializer
# Create your views here.

class DisciplinasDiurnoList(generics.ListCreateAPIView):

    queryset = DisciplinasDiurno.objects.all()
    serializer_class = DisciplinasDiurnoSerializer
