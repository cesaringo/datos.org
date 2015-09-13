(function(){
	'use strict';
	var app = angular.module('ChartSEP', ['ngMaterial', 'ui.router', 'chart.js'])
	.config(function($stateProvider, $urlRouterProvider){
		$stateProvider
		.state('home', {
			url: '/',
			templateUrl: '/static/views/home.html',
			controller: 'HomeCtrl'
		})
		.state('charts',{
			url: '/charts',
			abstract: true,
			templateUrl: "/static/views/charts/charts.html",
		})
		.state('charts.eficiencia-terminal', {
			url: '/eficiencia-terminal',
			templateUrl: '/static/views/charts/eficiencia-terminal.html',
			controller: 'ChartEficienciaTerminalCtrl',
			controllerAs: 'et'
		})
		.state('charts.mujeres-en-ingenieria', {
			url: '/mujeres-en-ingenieria',
			templateUrl: '/static/views/charts/mujeres-en-ingenieria.html',
			controller: 'ChartMujeresEnIngenieria',
			controllerAs: 'mi',
		})
		.state('encuentra-tu-universidad',{
			url: '/encuentra-tu-universidad',
			templateUrl: '/static/views/encuentra-tu-universidad.html',
			controller: 'EncuentraUniversidadCtrl',
			controllerAs: 'bu',
		});

		$urlRouterProvider.otherwise('/');
	});

	//Controllers
	app
	.controller('AppCtrl', function($scope){
		console.log("ChartSEP app");
	})

	.controller('HomeCtrl', function($scope){
		console.log("ChartSEP Home");
	})

	.controller('ChartEficienciaTerminalCtrl', function($scope, SEPChartService){
		console.log('ChartEficienciaTerminalCtrl');
		var self = this;
		$scope.loading = true;
		$scope.entidades_federativas = [];
		$scope.ciclos_escolares = [];
		$scope.current_entidades_federativas = [];
		$scope.curret_ciclos_escolares = [];
		self.niveles = ['preescolar', 'primaria', 'secundaria', 'media superior', 'superior']
		self.ChangeNivel = ChangeNivel;
		$scope.porcentaje_de_terminacion = [];

		$scope.LoadChart = function (){
			if (queryCiclo == 'all')
				$scope.current_ciclos_escolares = $scope.ciclos_escolares;
			else
				$scope.current_ciclos_escolares = (typeof queryCiclo == 'string')? [queryCiclo]: queryCiclo
			
			if (queryEstado == 'all')
				$scope.current_entidades_federativas = $scope.entidades_federativas;
			else
				$scope.current_entidades_federativas = (typeof queryEstado == 'string')? [queryEstado]: queryEstado


			$scope.loading = true;
			SEPChartService.PorcentajeDeTerminacion(queryEstado, queryCiclo, queryNivel)
			.then(function(response){
				$scope.loading = false;
				$scope.porcentaje_de_terminacion = response.data;
				if ($scope.porcentaje_de_terminacion.length == 0){
					alert('No existen datos');
					$scope.current_ciclos_escolares = [];
					$scope.current_entidades_federativas = [];
				}
				//console.log($scope.porcentaje_de_terminacion);
			}, function(response){
			});
		};
		var queryEstado = 'all';
		var queryCiclo = 'all';
		var queryNivel = 'all';


		SEPChartService.EntidadesFederativas('all')
		.then(function(response){
			$scope.entidades_federativas = response.data;
			$scope.current_entidades_federativas = response.data;
			self.estados = CargarEstados();
			self.querySearch   = querySearch;
			self.ChangeEstado = ChangeEstado;
			self.searchTextChange   = searchTextChange;

			SEPChartService.CiclosEscolares('all')
			.then(function(response){
				$scope.ciclos_escolares = response.data;
				$scope.current_ciclos_escolares = response.data;
				self.ciclos_escolares = $scope.ciclos_escolares;
				self.ChangeCicloEscolar = ChangeCicloEscolar;
				$scope.LoadChart();
			}, function(response){
			//Error
			});
		}, function(response){
				//Error
		});
		function CargarEstados(){
			var entidades_federativas = $scope.entidades_federativas;
			return entidades_federativas;
		}
		function querySearch (query) {
			var results = query ? self.estados.filter( createFilterFor(query) ) : self.estados;
			return results;
		}
		function createFilterFor(query) {
			var lowercaseQuery = angular.lowercase(query);
			return function filterFn(estado) {
				return (estado.indexOf(lowercaseQuery) === 0);
			};
		}
		function searchTextChange(text) {
      		//console.log('Text changed to ' + text);
    		}
    		function ChangeEstado(item) {
    			if (item == null || item == undefined)
    				queryEstado = 'all';
    			else
    				queryEstado = item;
    		}
    		function ChangeCicloEscolar(item){
    			if (item == null || item == undefined)
    				queryCiclo = 'all';
    			else
    				queryCiclo = item;

    		}
    		function ChangeNivel(item){
    			if (item == null || item == undefined)
    				queryNivel = 'all';
    			else
    				queryNivel = item;
    		}
	})
	.controller('ChartMujeresEnIngenieria', function($scope, SEPChartService){
		$scope.entidades = [];
		$scope.ciclos = [];
		$scope.data = [];
		$scope.loading = true;

		$scope.query_ciclos = 'all';
		$scope.query_entidades = 'all';

	

		SEPChartService.MEIEntidades()
		.then(function(response){
			$scope.entidades = response.data;
			$scope.current_entidades = response.data;
			SEPChartService.MEICiclos()
			.then(function(response){
				$scope.ciclos = response.data;
				$scope.currenr_ciclos = response.data;
				$scope.LoadChart($scope.query_entidades, $scope.query_ciclos);
			}, function(response){
			})
		}, function(response){

		});

		$scope.LoadChart = function(entidades, ciclos){
			$scope.loading = true;
			SEPChartService.MEIPorcentajeDeMujeres(entidades, ciclos)
			.then(function(response){
				$scope.data = response.data;
				$scope.loading = false;
			}, function(response){

			})
		}

		$scope.ChangeEntidad = function (item) {
    			if (item == null || item == undefined){
    				$scope.current_entidades = $scope.entidades;
    				$scope.query_entidades = 'all';
    			}
    			else{
    				$scope.current_entidades = [item];
    				$scope.query_entidades = item;
    			}
    			$scope.LoadChart($scope.query_entidades, $scope.query_ciclos);
    		}

    		$scope.ChangeCiclo = function (item){
    			if (item == null || item == undefined){
    				$scope.current_ciclos = $scope.ciclos;
    				$scope.query_ciclos = 'all';
    			}
    			else{
    				$scope.current_ciclo = [item];
    				$scope.query_ciclos = item;
    			}
    			$scope.LoadChart($scope.query_entidades, $scope.query_ciclos);
    		}


	})
	.controller('EncuentraUniversidadCtrl', function($scope, $mdDialog, SEPChartService){
		console.log('EncuentraUniversidadCtrl');
		$scope.universidades = []
		$scope.buscando = false;
		var alert;
		$scope.params = {
			publica: true,
			privada: true,
			programa: '',
			institucion: '',
			entidad_federativa: ''
		}
		
		

		$scope.programas_educativos = [];
		$scope.entidades = [];

		SEPChartService.getEntidadesUniversidad()
		.then(function(response){
			$scope.entidades = response.data;
		},function(response){})

		SEPChartService.getProgramasEducativos()
		.then(function(response){
			$scope.programas_educativos = response.data;
		},function(response){})

		$scope.CambiarPrograma = function(item){
			$scope.params.programa = item;
		};

		$scope.getProgramasEducativos = function (query) {
			console.log(query);
			var results = query ? $scope.programas_educativos.filter(createFilterFor(query)) : $scope.programas_educativos;
			return results;
		};
		function createFilterFor(query) {
			var lowercaseQuery = angular.lowercase(query);
			return function filterFn(programas_educativo) {
				return (programas_educativo.indexOf(lowercaseQuery) === 0);
			};
		}
		function searchTextChange(text) {
      		//console.log('Text changed to ' + text);
    		}

    		$scope.ChangeEntidad = function (item) {
    			$scope.params.entidad_federativa = item;
    		};

    		$scope.BuscarUniversidades = function(params){
    			$scope.buscando = true;
    			SEPChartService.BuscarUniversidades(params)
    			.then(function(response){
    				$scope.universidades = response.data;
    				$scope.buscando = false;
    			}, function(response){})
    		};
    		$scope.openInfo = function(event, institucion){
    			SEPChartService.UniversidadInfo(institucion)
    			.then(function(response){
    				$scope.carreras = response.data;
    				$scope.showAlert(event, $scope.carreras, institucion);
    			}, function(response){})
    		};

    		$scope.showAlert = function(ev, carreras, institucion) {
    			console.log(carreras);
			// Appending dialog to document.body to cover sidenav in docs app
			// Modal dialogs should fully cover application
			// to prevent interaction outside of dialog
			$mdDialog.show(
			 $mdDialog.alert()
			   .parent(angular.element(document.querySelector('#popupContainer')))
			   .clickOutsideToClose(true)
			   .title(institucion)
			   .content(carreras.toString())
			   .ariaLabel('Planes educativos de la unversidad')
			   .ok('Ok!')
			   .targetEvent(ev)
			);
		};

    		

	})
	
	function DialogController($scope, $mdDialog) {
		$scope.hide = function() {
		$mdDialog.hide();
		};
		$scope.cancel = function() {
		$mdDialog.cancel();
		};
		$scope.answer = function(answer) {
		$mdDialog.hide(answer);
		};
	}

	//Services
	app.service('SEPChartService', function($q, $http){
		return {
			CiclosEscolares: function(query){
				return $http.get('http://localhost:8000/sep-api/ciclos-escolares/')
			},
			EntidadesFederativas: function(query){
				return $http.get('http://localhost:8000/sep-api/entidades-federativas/')
			},
			PorcentajeDeTerminacion: function(entidades, ciclos, nivel){
				return $http.get('http://localhost:8000/sep-api/obtener-eficiencia-terminal/',
				{
					params : {entidades_federativas: entidades, ciclos: ciclos, nivel: nivel}
				})
			},

			MEIEntidades: function(){
				return $http.get('http://localhost:8000/sep-api/mei-entidades/')
			},
			MEICiclos: function(){
				return $http.get('http://localhost:8000/sep-api/mei-ciclos-escolares/')
			},
			MEIPorcentajeDeMujeres: function(entidades, ciclos){
				return $http.get('http://localhost:8000/sep-api/mei-porcentaje/',{
					params : {entidades: entidades.toString(), ciclos: ciclos.toString() }
				})
			},

			getProgramasEducativos: function(){
				return $http.get('http://localhost:8000/sep-api/programas-educativos/')
			},

			getEntidadesUniversidad: function(){
				return $http.get('http://localhost:8000/sep-api/entidades-universidades/')
			},
			BuscarUniversidades: function(params){
				return $http.get('http://localhost:8000/sep-api/buscar-universidad/', {
					params: params
				})
			},
			UniversidadInfo: function(institucion){
				return $http.get('http://localhost:8000/sep-api/universidad-info/', {
					params: {institucion: institucion}
				})
			}
		}
	});

	app.filter('capitalize', function() {
		return function(input) {
		 return (!!input) ? input.charAt(0).toUpperCase() + input.substr(1).toLowerCase() : '';
		}
	});


	
})();