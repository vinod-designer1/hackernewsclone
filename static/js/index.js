var app = angular.module('NewsApp', ['ngMaterial', 'ngAnimate']);

app.controller('mainCtrl', ['$scope', '$http', '$mdDialog', '$window',
  function($scope, $http, $mdDialog, $window){
    $scope.login_details = {
      username:'',
      password:''
    };

    $scope.getCookie = function (c_name)
    {
      if (document.cookie.length > 0)
      {
          c_start = document.cookie.indexOf(c_name + "=");
          if (c_start != -1)
          {
              c_start = c_start + c_name.length + 1;
              c_end = document.cookie.indexOf(";", c_start);
              if (c_end == -1) c_end = document.cookie.length;
              return unescape(document.cookie.substring(c_start,c_end));
          }
      }
      return "";
    };

    $scope.login = function($event) {
      $http.defaults.headers.post["X-CSRFToken"] = $scope.getCookie("csrftoken");
      $http.defaults.headers.post["Content-Type"] = "application/json";
      $http.post('/login/', $scope.login_details)
           .success(function(data, status, headers, config){
              $window.location.reload();
           })
           .error(function(data, status, headers, config) {
             $mdDialog.show(
                $mdDialog.alert()
                  .parent(angular.element(document.body))
                  .title('Login Error!')
                  .content('Wrong username and password!')
                  .ariaLabel('Login Error Dialog')
                  .ok('Ok')
                  .targetEvent($event)
              );
           });

    };

    $scope.logout = function ($event) {
      $window.location = '/logout';
    };

    $scope.register = function($event) {
      $http.defaults.headers.post["X-CSRFToken"] = $scope.getCookie("csrftoken");
      $http.defaults.headers.post["Content-Type"] = "application/json";
      $http.post('/register/', $scope.login_details)
           .success(function(data, status, headers, config){
              $mdDialog.show(
                $mdDialog.alert()
                  .parent(angular.element(document.body))
                  .title('Register Success!')
                  .content('Registratio successful please login!')
                  .ariaLabel('Register Success Dialog')
                  .ok('Ok')
                  .targetEvent($event)
              );
           })
           .error(function(data, status, headers, config) {
             $mdDialog.show(
                $mdDialog.alert()
                  .parent(angular.element(document.body))
                  .title('Register Error!')
                  .content('Username already taken!')
                  .ariaLabel('Register Error Dialog')
                  .ok('Ok')
                  .targetEvent($event)
              );
           });
    };

}]);