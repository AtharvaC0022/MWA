var app = angular.module("AlumniApp", []);

app.controller("AlumniController", function($scope) {

    $scope.saveData = function() {
        let alumniList = JSON.parse(localStorage.getItem("alumniData")) || [];
        alumniList.push($scope.alumni);
        localStorage.setItem("alumniData", JSON.stringify(alumniList));
        alert("Alumni registered successfully!");
        $scope.alumni = {}; 
    };

    $scope.alumniList = JSON.parse(localStorage.getItem("alumniData")) || [];
});
