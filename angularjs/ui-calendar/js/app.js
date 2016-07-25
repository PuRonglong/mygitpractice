var myApp = angular.module('myApp', ['ui.router', 'ngAnimate']);

myApp.controller('viewController', function(){
	this.current = '1';
});