 /* Controllers */
angular.module('myApp.controllers', [])
	.controller('myTimelineController', ['$scope','$http', function($scope,$http) {
			$http.get('/timeline').success(function(data){
				var name, pic, desc, bg;

				$scope.timeline = data;

				name = $scope.timeline.name;
				document.getElementById("header").innerHTML = name; 

				pic = $scope.timeline.profile_image_url.replace('_normal','');
				document.getElementById("img").src = pic; 

				desc = $scope.timeline.description;
				document.getElementById("bio").innerHTML = desc; 

				bg = $scope.timeline.profile_background_image_url;
				document.getElementById("background").style.background = 'url(' + bg + ') no-repeat 50% 50%'; 
				
			});
		}])

	.controller('myTweetController', ['$scope','$http', function($scope,$http) {
			
			$http.get('/tweets').success(function(data){
				$scope.tweets = data["tweet_array"];
			});

			$scope.limit = 10;

		}]);
