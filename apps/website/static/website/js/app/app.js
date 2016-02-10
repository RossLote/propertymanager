!function(){
    var app = window.PropertiesApp = angular.module('PropertiesApp', ['ngRoute', 'ngResource']);
    app.config(['$resourceProvider', function($resourceProvider) {
      // Don't strip trailing slashes from calculated URLs
      $resourceProvider.defaults.stripTrailingSlashes = false;
    }]);

    app.config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }]);
}()
