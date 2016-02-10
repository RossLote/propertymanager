!function(app){
    var base = 'static/website/html/properties/'
    app.config(['$routeProvider',
      function($routeProvider) {
        $routeProvider.
          when('/properties', {
            templateUrl: base+'list.html',
            controller: 'PropertiesListCtrl'
          }).
          when('/properties/add', {
            templateUrl: base+'new.html',
            controller: 'PropertiesAddCtrl'
          }).
          when('/properties/:id/edit', {
            templateUrl: base+'new.html',
            controller: 'PropertiesEditCtrl'
          }).
          otherwise({
            redirectTo: '/'
          });
    }])

    .controller('PropertiesListCtrl', ['$scope', '$resource',function($scope, $resource){
        var api = $resource('/api/v1/properties/');
        $scope.properties = api.query();
    }])

    .controller('PropertiesAddCtrl', ['$scope', '$resource', function($scope, $resource){
        var api = $resource('/api/v1/properties/');
        $scope.property = {};

        $scope.createProperty = function(){
            api.save($scope.property, function(property){
                console.log(arguments, 'Saved');
            });
        };
    }])

    .controller('PropertiesEditCtrl', ['$scope', '$resource', '$routeParams', function($scope, $resource, $routeParams){

    }]);

}(PropertiesApp);
