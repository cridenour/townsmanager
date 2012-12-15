var app = angular.module('towns', ['ui'])

app.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', {templateUrl: 'templates/home.html',   controller: HomeViewController}).
        when('/campaigns', {templateUrl: 'templates/campaign.html', controller: CampaignController}).
        otherwise({redirectTo: '/'});
    }])

// Set UI Tooltip options
app.value('ui.config', {
        jq: {
            tooltip: {
                placement: 'bottom'
            }
        }
    });

window.editor = {}