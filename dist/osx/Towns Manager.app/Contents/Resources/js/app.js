// create and set menu
var menu = Ti.UI.createMenu(),
    fileItem = Ti.UI.createMenuItem('File'),
    exitItem = fileItem.addItem('Exit', function() {
      if (confirm('Are you sure you want to quit?')) {
        Ti.App.exit();
      }
    });

menu.appendItem(fileItem);
Ti.UI.setMenu(menu);

setTimeout(function() { Ti.UI.showDialog({
  url:'app://dialog.html',
  y: 400,
  x: 200,
  height: 500,
  width: 100
}); }, 2000);