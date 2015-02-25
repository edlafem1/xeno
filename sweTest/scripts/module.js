var demoApp = angular.module('demoApp', ['ngRoute']); // [] means no dependencies for this module
    
    // Usually have a 1 to 1 ratio of controllers to views
    demoApp.config(function ($routeProvider) {
        $routeProvider
            .when('/view1',
                  {
                      controller: 'SimpleController',
                      templateUrl: 'Partials/View1.html'
                  })
            .when('/view2',
                  {
                      controller: 'SimpleController',
                      templateUrl: 'Partials/View2.html'
                  })
            .when('/view3',
                  {
                      controller: 'SimpleController',
                      templateUrl: 'Partials/View3.html'
                  })
            .otherwise({ redirectTo: '/view1' });
    });

    demoApp.factory('simpleFactory', function(/*$http for http calls*/) {
        var cusomters = [
            {name: 'Lamborghini', city: 'Reventon'},
            {name: 'Lamborghini', city: 'Veneno'},
            {name: 'McLaren', city:'650S Spider'},
            {name: 'Ferrari', city:'488 GTB'},
            {name: 'Bagger', city:'288'},
            {name: 'Bugatti', city:'Veyron'},
            {name: 'Acura', city:'NSX'},
            {name: 'Toyota', city:'Corolla'}
        ];

        var factory = {};
        factory.getCustomers = function() {
            return cusomters;
        };
        factory.putCustomer = function(customer) {

        };

        return factory;
    });

    /*
    var controllers = {};
    controllers.SimpleController = function SimpleController($scope) {
        $scope.customers= [
            {name: 'Michael Bishoff', city: 'Clarksville'},
            {name: 'Ai Onda', city: 'Gaithersburg'},
            {name:'Minhaz Mahmud', city:'Catonsville'},
            {name:'George Allison', city:'Catonsville'}
        ];
    };
    demoApp.controller(controllers);
    */

    demoApp.controller('SimpleController', function SimpleController($scope, simpleFactory) {
        $scope.customers = []; // simpleFactory.getCustomers();

        init();

        function init() {
            $scope.customers = simpleFactory.getCustomers();
        }
        /* If you do it this way, then the customers will only be local to the View
            {name: 'Michael Bishoff', city: 'Clarksville'},
            {name: 'Ai Onda', city: 'Gaithersburg'},
            {name:'Minhaz Mahmud', city:'Catonsville'},
            {name:'George Allison', city:'Catonsville'}
        ];
        */
        $scope.addCustomer = function () {
            $scope.customers.push(
                {
                    name: $scope.newCustomer.name,
                    city: $scope.newCustomer.city
                });
        };
    });