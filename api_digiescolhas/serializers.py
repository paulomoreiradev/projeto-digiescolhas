from rest_framework import serializers
from app_digiescolhas.models import DisciplinasDiurno

class DisciplinasDiurnoSerializer(serializers.ModelSerializer):


    class Meta:

        model = DisciplinasDiurno
        fields = '__all__'