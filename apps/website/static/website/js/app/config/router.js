!function(app){
    var base = 'static/website/html/'
    app.config(['$routeProvider',
      function($routeProvider) {
        $routeProvider.
          when('/', {
            templateUrl: base+'/home.html',
            controller: 'DashboardCtrl'
          }).
          when('/properties', {
            templateUrl: base+'properties.html',
            controller: 'PropertiesCtrl'
          }).
          otherwise({
            redirectTo: '/'
          });
    }]);
}(PropertyApp);
