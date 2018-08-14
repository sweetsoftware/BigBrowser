var page = require('webpage').create();
var system = require('system')
//var fs = require('fs');

page.viewportSize = { width: 1024, height: 1024 };
page.clipRect = { top: 0, left: 0, width: 1024, height: 768 };
page.open(system.args[1], function() {
  
  setTimeout(function(){
    page.render(system.args[2]);
    //fs.write('index.html', page.content, 'w');
    phantom.exit();
  }, 4000);
});

