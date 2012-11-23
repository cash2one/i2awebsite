#!/bin/sh
DIR_JS=static/js
DIR_CSS=static/css
jsmin < $DIR_JS/scripts.js > $DIR_JS/scripts.min.js
cssmin < $DIR_CSS/style.css > $DIR_CSS/style.min.css
cssmin < $DIR_CSS/nivo-skin.css > $DIR_CSS/nivo-skin.min.css
cssmin < $DIR_CSS/nivo-slider.css > $DIR_CSS/nivo-slider.min.css
