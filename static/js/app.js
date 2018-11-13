let app = angular.module("app", []);

app.controller('MainController', ($document, $scope, $http) => {

	$scope.languages = [];

	$scope.from = null;
	$scope.to = null;

	$scope.search = "";
	$scope.result = "";

	$scope.initLanguages = () => {
		$http({
			method: 'GET',
			url: '/a'
		}).then((response) => {
			$scope.languages = response.data;
		})
	};

	(() => {
		$scope.initLanguages()
	})();

	$scope.updateSearch = () => {
		$scope.result = $scope.search
	};

});