from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EntidadesFederativasSerializer
from .models import EficienciaTerminal, PorcentajeMujeresIngenieria, Universidades
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class ListarEntidadesFederativas(APIView):
	def get(self, request, format=None):
		entidades_federativas = EficienciaTerminal.objects.values_list('entidad_federativa', flat=True).distinct()
		return Response (entidades_federativas)

class ListarCiclosEscolares(APIView):
	def get(self, request, format=None):
		ciclos_escolares = EficienciaTerminal.objects.values_list('ciclo_escolar', flat=True).distinct()
		return Response (ciclos_escolares)


class ObetenerEficienciaTerminal(APIView):
	def get(self, request, format=None):
		if request.GET.get('entidades_federativas') is None or request.GET.get('entidades_federativas') == 'all':
			entidades = EficienciaTerminal.objects.values_list('entidad_federativa', flat=True).distinct()
		else: 
			requestedEstados = request.GET.get('entidades_federativas').split(',')
			entidades = EficienciaTerminal.objects.filter(entidad_federativa__in = requestedEstados).values_list('entidad_federativa', flat=True).distinct()

		#No params
		if request.GET.get('ciclos') is None or request.GET.get('ciclos') == 'all':
			ciclos = EficienciaTerminal.objects.values_list('ciclo_escolar', flat=True).distinct()
		else:
			requestedCiclos = request.GET.get('ciclos').split(',')
			ciclos = EficienciaTerminal.objects.filter(ciclo_escolar__in = requestedCiclos).values_list('ciclo_escolar', flat=True).distinct()


		data = EficienciaTerminal().porcentaje_por_estados(entidades, ciclos, request.GET.get('nivel'))
		return Response(data)

class MEIListarEntidades(APIView):
	def get(self, request, format=None):
		entidades = PorcentajeMujeresIngenieria.objects.values_list('entidad', flat=True).distinct()
		return Response (entidades)

class MEIListarCiclos(APIView):
	def get(self, request, format=None):
		ciclos = PorcentajeMujeresIngenieria.objects.values_list('ciclo', flat=True).distinct()
		return Response (ciclos)

class MEIPorcentaje(APIView):
	def get(self, request, format=None):
		if request.GET.get('entidades') is None or request.GET.get('entidades') == 'all':
			entidades = PorcentajeMujeresIngenieria.objects.values_list('entidad', flat=True).distinct()
		else:
			entidades_requeridas = request.GET.get('entidades').split(',')
			entidades = PorcentajeMujeresIngenieria.objects.filter(entidad__in = entidades_requeridas).values_list('entidad', flat=True).distinct()

		if request.GET.get('ciclos') is None or request.GET.get('ciclos') == 'all':
			ciclos = PorcentajeMujeresIngenieria.objects.values_list('ciclo', flat=True).distinct()
		else:
			ciclos_requeridos = request.GET.get('ciclos').split(',')
			ciclos = PorcentajeMujeresIngenieria.objects.filter(ciclo__in = ciclos_requeridos).values_list('ciclo', flat=True).distinct()

		data = PorcentajeMujeresIngenieria().porcentaje(entidades, ciclos)
		return Response(data)

class EncontrarUniversidad(APIView):
	def get(self, request, format=None):
		params = request.GET
		print params
		universidades = Universidades().buscar_universidades(params)
		return Response(universidades)

class ProgramasEducativos(APIView):
	def get(self, request, format=None):
		programas_educativos = Universidades.objects.values_list('programa', flat=True).distinct()
		return Response(programas_educativos)

class EntidadesUniversidades(APIView):
	def get(self, request, format=None):
		entidades = Universidades.objects.values_list('entidad_federativa', flat=True).distinct()
		return Response(entidades)

class UniversidadInfo(APIView):
	def get(self, request, format=None):
		carreras = Universidades.objects.filter(institucion=request.GET.get('institucion', '')).values_list('programa', flat=True).distinct()
		return Response(carreras)