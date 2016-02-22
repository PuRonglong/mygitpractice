var myApp = angular.module('myApp', ['ui.router', 'ngAnimate']);

myApp.controller('viewController', viewController);

function  viewController(){
	this.current = '1';
}