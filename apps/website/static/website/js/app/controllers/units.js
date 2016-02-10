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
        $scope.units = api.query({
            property: $routeParams.propertyID
        });
    }])

    .controller('UnitsEditCtrl', ['$scope', '$resource', '$routeParams',function($scope, $resource, $routeParams){
        var api = $resource('/api/v1/units/:id');
        $scope.unit = api.get({
            id: $routeParams.unitID
        });
    }]);

}(PropertiesApp);
