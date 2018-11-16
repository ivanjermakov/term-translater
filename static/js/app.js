let app = angular.module("app", []);

app.controller('MainController', ($document, $scope, $http) => {

	$scope.SEARCH_RESULTS_AMOUNT = 5;

	$scope.languages = [];

	$scope.from = null;
	$scope.to = null;

	$scope.search = "";
	$scope.result = "";

	$scope.suggestions = [];

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
		let currentSearch = $scope.search;

		setTimeout(() => {
			if (currentSearch === $scope.search) {
				$http({
					method: 'GET',
					url: '/s',
					params: {
						"l": $scope.from,
						"s": $scope.search
					}
				}).then((response) => {
						$scope.suggestions = response.data;
						$scope.suggestions = $scope.suggestions.slice(0, $scope.SEARCH_RESULTS_AMOUNT)
					}
				)
			}
		}, 200);
	};

	$scope.translate = (suggestion) => {
		$http({
			method: 'GET',
			url: '/t',
			params: {
				"from": $scope.from,
				"to": $scope.to,
				"title": suggestion
			}
		}).then((response) => {
			$scope.result = response.data;
		})
	};

});