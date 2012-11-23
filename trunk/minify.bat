@echo off
cd static\js
jsmin < function.js > function.min.js
jsmin < jquery.client.js > jquery.client.min.js
jsmin < jquery.corner.js > jquery.corner.min.js
jsmin < jquery.cycle.all.js > jquery.cycle.all.min.js
jsmin < jquery.tooltip.js > jquery.tooltip.min.js
jsmin < jquery.cookie.js > jquery.cookie.min.js
jsmin < queryLoader.js > queryLoader.min.js
cd ..\..