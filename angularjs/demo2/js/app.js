var myApp = angular.module('myApp', ['ngRoute', 'ngAnimated']);

//现在，我们创建了我们的程序、路由以及控制器。
//每一个控制器都有一个它自己的pageClass变量。改变了的值会被添加到index.html文件中的ng-view中，这样我们的每一个页面都有了不同的类名。
//通过这些不同的类名，我们可以为不同的页面添加不同的动画效果。

myApp.config(['$routerProvider', function($routeProvider){
	$routeProvider
			.when('/', {
				templateUrl: 'Page-home.html',
				controller: 'homeController'
			})
			.when('/about', {
				templateUrl: 'Page-about.html',
				controller: 'aboutController'
			})
			.when('/contact', {
				templateUrl: 'Page-contact.html',
				controller: 'contactController'
			})

			.otherwise({redirectTo: '/'});
}]);

myApp.controller('homeController', function($scope){
	$scope.pageClass = 'page-home';
});

myApp.controller('aboutController', function($scope){
	$scope.pageClass = 'page-about';
});

myApp.controller('contactController', function($scope){
	$scope.pageClass = 'page-contact'
});