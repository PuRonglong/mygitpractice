var myApp = angular.module('myApp', ['ui.router']);

myApp.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider){
	$stateProvider
		.state('PageTab',{
			url: '/PageTab',
			templateUrl: 'PageTab.html'
		})
		.state('PageTab.Page1', {
			url: '/Page1',
			templateUrl: 'Page-1.html'
		})
		.state('PageTab.Page2', {
			url: '/Page2',
			templateUrl: 'Page-2.html'
		})
		.state('PageTab.Page3', {
			url: '/Page3',
			templateUrl: 'Page-3.html'
		});

	$urlRouterProvider.when("", "/PageTab");
}]);
