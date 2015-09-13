import rest_framework
from rest_framework import serializers
from .models import EficienciaTerminal

# class EficienciaTerminalSerializer(serializers.ModelSerializer):
# 	entidad_federativa = serializers.CharField(write_only=True)
# 	class Meta:
# 		model = EficienciaTerminal
# 		fields = ['entidad_federativa',]
		
class EntidadesFederativasSerializer(serializers.Serializer):
	entidad_federativa = serializers.CharField(write_only=True)

	

