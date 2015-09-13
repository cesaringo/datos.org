from django.db import models
from django.db.models import Sum
from django.db.models import Q

class Chart(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()

class EficienciaTerminal(models.Model):
	"""
	Eficiencia terminal por nivel educativo
	"""
	NIVEL_EDUCATIVO = (
		('01 PRESCOLAR', 'PRESCOLAR'), 
		('02 PRIMARIA', 'PRIMARIA'),
		('03 SECUNDARIA', 'SECUNDARIA'),
		('05 MEDIA SUPERIOR', 'MEDIA SUPERIOR'),
		('06 SUPERIOR', 'SUPERIOR')
	)
	entidad_federativa = models.CharField(max_length=100)
	nivel_educativo = models.CharField(choices=NIVEL_EDUCATIVO, max_length=50)
	servicio_educativo = models.CharField(max_length=100)
	num_municipio = models.IntegerField()
	nombre_municipio = models.CharField(max_length=100)
	ciclo_escolar = models.CharField(max_length=50)
	nuevos_ingresos = models.IntegerField(null=True)
	egresados = models.IntegerField(null=True)
	eficiencia_terminal = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)


	def save(self, *args, **kwargs):
		if  self.nuevos_ingresos and self.egresados and  self.nuevos_ingresos > 0:
			self.eficiencia_terminal = self.egresados * 1.0 / self.nuevos_ingresos
		else:
			self.eficiencia_terminal = -1
		super(EficienciaTerminal, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.egresados) + '/' + str(self.nuevos_ingresos) + '=' + str(self.eficiencia_terminal)


	def porcentaje_por_estados(self, entidades_federativa, ciclos_escolares, nivel):
		data = []
		for ciclo_escolar in ciclos_escolares:
			row = []
			for entidad_federativa in entidades_federativa:
				if nivel is None or nivel == 'all':
					items = EficienciaTerminal.objects.filter(entidad_federativa = entidad_federativa, ciclo_escolar= ciclo_escolar)
				else:
					items = EficienciaTerminal.objects.filter(entidad_federativa = entidad_federativa, 
						ciclo_escolar= ciclo_escolar, 
						nivel_educativo__contains=nivel.upper()
					)

				if not items:
					return ([])

				nuevos_ingresos = items.aggregate(Sum('nuevos_ingresos')).get('nuevos_ingresos__sum')
				egresos = items.aggregate(Sum('egresados')).get('egresados__sum')
				porcentaje = 1.0 * egresos  / nuevos_ingresos 
				row.append(porcentaje)
			data.append(row)
		return data;


class PorcentajeMujeresIngenieria(models.Model):
	entidad = models.CharField(max_length=100)
	ciclo = models.CharField(max_length=50)
	mujeres = models.IntegerField()
	total = models.IntegerField()

	def porcentaje(self, entidades, ciclos):
		data = []
		for ciclo in ciclos:
			row = []
			for entidad in entidades:
				items = PorcentajeMujeresIngenieria.objects.filter(entidad=entidad, ciclo=ciclo)
				if not items:
					return ([])

				mujeres = items.aggregate(Sum('mujeres')).get('mujeres__sum')
				total = items.aggregate(Sum('total')).get('total__sum')
				porcentaje = 1.0 * mujeres / total
				row.append(porcentaje)
			data.append(row)
		return data

def xstr(s):
    if s is None:
        return ''
    return str(s)

class Universidades(models.Model):
	programa = models.CharField(max_length=200)
	institucion = models.CharField(max_length=200)
	entidad_federativa = models.CharField(max_length=100)
	clave_entidad = models.IntegerField()
	sostenimiento = models.CharField(max_length=100)
	tipo = models.CharField(max_length=100)

	def get_sostenimiento(self, publica, privada):
		if publica == 'true' and privada=='true':
			return ''
		if not publica == 'true' and not privada == 'true':
			return 'null'
		if publica == 'true':
			return 'Publico'
		if privada == 'true':
			return 'Particular'

	def buscar_universidades(self, params):
		#Params
		sostenimiento = self.get_sostenimiento(params.get('publica'), params.get('privada'))
		print sostenimiento

		universidades = Universidades.objects.filter(
			Q(institucion__contains=params.get('institucion', '').upper()),
			Q(programa__contains=params.get('programa', '').upper()),
			Q(entidad_federativa__contains=params.get('entidad_federativa', '')),
			Q(sostenimiento__contains=sostenimiento.capitalize()),
		).values_list('institucion',  flat=True).distinct()

		return universidades




		





