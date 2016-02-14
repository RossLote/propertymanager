!function(app){
    var base = 'static/website/html/units/'
    app.

    config(['$routeProvider',
      function($routeProvider) {
        $routeProvider.
          when('/properties/:propertyID/units', {
            templateUrl: base+'list.html',
            controller: 'UnitsListCtrl'
          }).
          when('/properties/:propertyID/units/add', {
            templateUrl: base+'new.html',
            controller: 'UnitsAddCtrl'
          }).
          when('/properties/:propertyID/units/:unitID', {
            templateUrl: base+'edit.html',
            controller: 'UnitsEditCtrl'
          }).
          otherwise({
            redirectTo: '/'
          });
    }])

    .controller('UnitsListCtrl', ['$scope', '$resource', '$routeParams',function($scope, $resource, $routeParams){
        var api = $resource('/api/v1/units/');
        var propertyAPI = $resource('/api/v1/properties/:id/');
        $scope.property = propertyAPI.get({
            id: $routeParams.propertyID
        });
        $scope.units = api.query({
            property: $routeParams.propertyID
        });
    }])

    .controller('UnitsAddCtrl', ['$scope', '$resource', '$routeParams',function($scope, $resource, $routeParams){
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

    .controller('UnitsEditCtrl', ['$scope', '$resource', '$routeParams',function($scope, $resource, $routeParams){
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
