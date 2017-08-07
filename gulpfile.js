
var gulp = require('gulp');
var gutil = require('gulp-util');
var babelify = require('babelify');
var reactify = require('reactify');
var del = require('del');
var sass = require('gulp-sass');
var webpack = require("webpack");
var webpack_stream = require("webpack-stream");
const webpack_config = require('./webpack.config.js');



gulp.task('sass', function () {
  return gulp.src('./static/app/src/css/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./static/app/src/css/'));
});


gulp.task('transform', function () {
    return webpack_stream(webpack_config)
        .pipe(gulp.dest('static/app/src/dist/'));
});

gulp.task('build', function () {
    gulp.start('sass');
    gulp.start('transform');
});

gulp.task('default', function () {
  gulp.start('sass');
  gulp.start('transform');
  gulp.watch('./static/app/src/css/*.scss', ['build']);
  gulp.watch('./static/app/src/scripts/*.js', ['build']);
});

