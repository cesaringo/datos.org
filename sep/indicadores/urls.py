from django.conf.urls import include, url, patterns
from .serializers import EntidadesFederativasSerializer
from .views import UniversidadInfo, EntidadesUniversidades, ProgramasEducativos, EncontrarUniversidad, MEIPorcentaje, MEIListarCiclos, ListarEntidadesFederativas, ListarCiclosEscolares, ObetenerEficienciaTerminal, MEIListarEntidades

urlpatterns = [
	url(r'^entidades-federativas/', ListarEntidadesFederativas.as_view(), name='entidades-federativas-list'),
	url(r'^ciclos-escolares/', ListarCiclosEscolares.as_view(), name='ciclos-escolares-list'),
	url(r'^obtener-eficiencia-terminal/', ObetenerEficienciaTerminal.as_view(), name='obtener-eficiencia-terminal'),

	url(r'^mei-entidades/', MEIListarEntidades.as_view(), name="mei-entidades"),
	url(r'^mei-ciclos-escolares/', MEIListarCiclos.as_view(), name="mei-ciclos-escolares"),
	url(r'^mei-porcentaje/', MEIPorcentaje.as_view(), name="mei-porcentaje"),

	url(r'^buscar-universidad/', EncontrarUniversidad.as_view(), name="encontrar-universidad"),
	url(r'^programas-educativos/', ProgramasEducativos.as_view(), name="programas-educativos"),
	url(r'^entidades-universidades/', EntidadesUniversidades.as_view(), name="entidades-universidades"),
	url(r'^universidad-info/', UniversidadInfo.as_view(), name="universidad-info"),
]
