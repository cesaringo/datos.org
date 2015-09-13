from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin
from import_export import fields
from .models import EficienciaTerminal, PorcentajeMujeresIngenieria, Universidades

class EficienciaTerminalAdminResource(resources.ModelResource):
	class Meta:
		model = EficienciaTerminal
		fields = ('id', 'entidad_federativa', 'nivel_educativo', 'servicio_educativo',
			'num_municipio', 'nombre_municipio', 'ciclo_escolar', 'nuevos_ingresos', 
			'egresados')

class EficienciaTerminalAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = EficienciaTerminalAdminResource

class PorcentajeMujeresIngenieriaAdminResource(resources.ModelResource):
	class Meta:
		model = PorcentajeMujeresIngenieria
		fields = ('id', 'entidad', 'ciclo', 'mujeres','total')

class PorcentajeMujeresIngenieriaAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = PorcentajeMujeresIngenieriaAdminResource
	
class UniversidadesAdminResource(resources.ModelResource):
	class Meta:
		model = Universidades
		fields = ('id', 'programa', 'institucion', 'entidad_federativa','clave_entidad', 'sostenimiento', 'tipo')

class UniversidadesAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = UniversidadesAdminResource
	

admin.site.register(EficienciaTerminal, EficienciaTerminalAdmin)
admin.site.register(PorcentajeMujeresIngenieria, PorcentajeMujeresIngenieriaAdmin)
admin.site.register(Universidades, UniversidadesAdmin)