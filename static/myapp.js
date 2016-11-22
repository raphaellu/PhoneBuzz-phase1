var phoneBuzzApp = angular.module('PhoneBuzzApp',[]);

phoneBuzzApp.controller('IndexCtrl', ['$scope', '$http', function($scope, $http) {
  	
  	$scope.submitGameInput = function(game) {
  		$http({
  			url : 'generate_phonebuzz.php',
  			method : "GET",
  			data : {
  				'number' : $scope.game.input
  			}
  		}).then(function(response) {
  			console.log(response.data);
  		});
  	}

}]);