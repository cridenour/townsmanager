function HomeViewController($scope) {

    $scope.files = window.editor.files;


    setTimeout(function () {
        $scope.needFolder = $scope.files.find_directory() === false
    }, 1000)

    $scope.changeFolder = function() {
        Ti.UI.openFolderChooserDialog(
            function(folders) {
                folder = folders[0]

                if(window.editor.setRoot(folder)) {
                    $scope.needFolder = false
                }
                else {
                    alert('That doesn\'t look like a valid towns folder.')
                }

            },
            {title:'Find the Towns Folder!'}
        )

    }

    $scope.playGame = function () {
        window.editor.playGame()
    }
}