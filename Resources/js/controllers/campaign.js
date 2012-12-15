function CampaignController($scope, $filter) {

    // Save a copy of our original python backend
    $scope.original = window.editor.loadCampaign()

    // Load our campaign
    $scope.campaign = angular.copy($scope.original)

    // Copy out default missions from Towns for ng-options
    $scope.defaultMissions = $.grep($scope.campaign.missions, function(e){ return e.baseType == null; });

    // Reset our changes
    $scope.resetCampaign = function() {
        $scope.campaign = angular.copy($scope.original)
    }

    // Utility function for duplicate ids - I hate this function with a fiery passion
    $scope.uniquesChecked = 0
    $scope.uniqueMissionId = function(id) {
        var result = $.grep($scope.campaign.missions, function(e){ return e.id == id; })

        // This result should be 1 during the original run through, but 0 during editing.
        if($scope.uniquesChecked < $scope.original.missions.length) {
            unique = result.length === 1
        } else {
            if(result.length && result[0].isNew) {
                unique = result.length === 1
            } else {
                unique = result.length === 0
            }
        }

        $scope.uniquesChecked++
        return unique
    }

    $scope.saveMissions = function(confirmed) {
        // First let's just check everything is valid
        if($.grep($scope.campaign.missions, function(e){ return e.id == undefined; }).length > 0) {
            $scope.errorMessage = "There are invalid ids. Please check your missions,"
            return;
        }

        // Was this called from our confirmation modal?
        if(confirmed === null)
            confirmed = false

        // Do we have any missions that were deleted?
        if(!confirmed && $filter('filter')($scope.campaign.missions, {'isDeleted': true}).length ) {
            $scope.saveConfirmationModalVisible = true
        }

        // Ok let's save this
        else {
            $scope.original = angular.copy($scope.campaign)
            // Actually save it!
            $scope.filename = window.editor.saveCampaign($scope.campaign)
            $scope.saved = true
        }

        // Close our modal if it was present
        if(confirmed)
            $scope.saveConfirmationModalVisible = false
    }

    // Set our sortable options
    $scope.sortableOptions = {
        handle: '.handle',
        revert: true,
        tolerance: 'pointer',
        placeholder: 'mission-placeholder'
    }
}

CampaignController.$inject = ['$scope','$filter']