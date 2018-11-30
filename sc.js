var page = require('webpage').create();
var system = require('system')

page.viewportSize = { width: 1024, height: 1024 };
page.clipRect = { top: 0, left: 0, width: 1024, height: 1024 };
page.settings.userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36';
page.settings.resourceTimeout = 5000;

page.open(system.args[1], function() {
  setTimeout(function() {
     page.render(system.args[2]);
     phantom.exit();
  }, 3000);
});

