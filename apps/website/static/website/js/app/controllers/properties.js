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
          when('/properties/:propertyID/edit', {
            templateUrl: base+'edit.html',
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
        var Property = $resource('/api/v1/properties/:id/',
            {id:'@id'}
        );
        $scope.property = new Property();

        $scope.createProperty = function(){
            $scope.property.$save(function(property){
                console.log(arguments, 'Saved');
            });
        };
    }])

    .controller('PropertiesEditCtrl', ['$scope', '$resource', '$routeParams', function($scope, $resource, $routeParams){
        var Property = $resource('/api/v1/properties/:id/',
            {id:'@id'},
            {
                'update': { method:'PUT' }
            }
        );
        $scope.property = Property.get({
            id: $routeParams.propertyID
        });

        $scope.updateProperty = function(){
            $scope.property.$update(function(property){
                console.log(arguments, 'Saved');
            });
        };
    }]);

}(PropertiesApp);
