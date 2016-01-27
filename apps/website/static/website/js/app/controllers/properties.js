!function(app){
    var base = 'static/website/html/'
    app.config(['$routeProvider',
      function($routeProvider) {
        $routeProvider.
          when('/properties', {
            templateUrl: base+'properties.html',
            controller: 'PropertiesCtrl'
          }).
          otherwise({
            redirectTo: '/'
          });
    }]);

    app.controller('PropertiesCtrl', ['$scope',function($scope){

    }]);

}(PropertiesApp);
