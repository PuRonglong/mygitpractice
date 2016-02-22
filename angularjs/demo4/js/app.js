var myApp = angular.module('myApp', ['ui.router', 'ngAnimate']);

myApp.controller('viewController', viewController);

function  viewController(){
	var view = this;
	view.current = '1';
}