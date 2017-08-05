var gulp = require('gulp');
var gulpBrowser = require("gulp-browser");
var reactify = require('reactify');
var del = require('del');
var size = require('gulp-size');


gulp.task('transform', function () {
  var stream = gulp.src('./static/app/scripts/*.js')
    .pipe(gulpBrowser.browserify({transform: ['reactify']}))
    .pipe(gulp.dest('./static/app/scripts/dist/'))
    .pipe(size());
  return stream;
});


gulp.task('default', function () {
  gulp.start('transform');
  gulp.watch('./static/app/scripts/*.js', ['transform']);
});



