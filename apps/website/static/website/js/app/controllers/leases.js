!function(app){
    var base = 'static/website/html/units/'
    app.

    config(['$routeProvider',
      function($routeProvider) {
        $routeProvider.
          when('/properties/:propertyID/units/:unitID/leases', {
            templateUrl: base+'edit.html',
            controller: 'LeaseEditCtrl'
          }).
          when('/properties/:propertyID/units/:unitID/leases/add', {
            templateUrl: base+'edit.html',
            controller: 'LeaseEditCtrl'
          }).
          when('/properties/:propertyID/units/:unitID/leases/:leaseID', {
            templateUrl: base+'edit.html',
            controller: 'LeaseEditCtrl'
          }).
          otherwise({
            redirectTo: '/'
          });
    }])

    .controller('LeaseListCtrl', ['$scope', '$resource', '$routeParams',function($scope, $resource, $routeParams){
        var api = $resource('/api/v1/units/');
        var propertyAPI = $resource('/api/v1/properties/:id/');
        $scope.property = propertyAPI.get({
            id: $routeParams.propertyID
        });
        $scope.units = api.query({
            property: $routeParams.propertyID
        });
    }])

    .controller('LeaseAddCtrl', ['$scope', '$resource', '$routeParams',function($scope, $resource, $routeParams){
        var Unit = $resource('/api/v1/units/:id/',
            {id:'@id'}
        );
        var Property = $resource('/api/v1/properties/:id/',
            {id:'@id'}
        );
        $scope.property = Property.get({
            id: $routeParams.propertyID
        });
        $scope.unit = new Unit();

        $scope.createUnit = function(){
            $scope.unit.property = $scope.property.id
            $scope.unit.$save(function(unit){
                console.log('Saved');
            });
        };
    }])

    .controller('LeaseEditCtrl', ['$scope', '$resource', '$routeParams',function($scope, $resource, $routeParams){
        var Unit = $resource('/api/v1/units/:id/',
            {id:'@id'},
            {
                'update': { method:'PUT' }
            }
        );
        var Property = $resource('/api/v1/properties/:id/',
            {id:'@id'}
        );
        $scope.property = Property.get({
            id: $routeParams.propertyID
        });
        $scope.unit = Unit.get({
            id: $routeParams.unitID
        });

        $scope.updateUnit = function(){
            $scope.unit.$update(function(unit){
                console.log('Saved');
            });
        };
    }]);

}(PropertiesApp);
