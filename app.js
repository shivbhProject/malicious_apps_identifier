var gplay = require('google-play-scraper');

var list = gplay.app({appId: 'com.google.android.apps.translate'})
//   .then(console.log, console.log);

console.log(list);