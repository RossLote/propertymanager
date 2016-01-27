!function(app){
    var base = 'static/website/html/'
    app.config(['$routeProvider',
      function($routeProvider) {
        $routeProvider.
          when('/', {
            templateUrl: base+'dashboard.html',
            controller: 'DashboardCtrl'
          }).
          otherwise({
            redirectTo: '/'
          });
    }]);

    app.controller('DashboardCtrl', ['$scope',function($scope){

    }]);

}(PropertiesApp);
