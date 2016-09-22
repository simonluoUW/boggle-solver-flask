angular.module('BoggleSolverApp', []).controller('BoggleSolverController', function($scope,$http) {
    $scope.boardSize = null
    $scope.random = function(size) {
        $scope.word_list = null
        $http.post('/api/random_board', {'size': size}).
            success(function(results) {
                $scope.board = results
            }).
            error(function(error) {
                console.log(error);
            });
    };

    $scope.solve = function(board) {
        $http.post('/api/solve', {'board':board}).
            success(function(results) {
                $scope.word_list = results
            }).
            error(function(error) {
                console.log(error);
            });
    };

});