
var path = require('path');
var webpack = require('webpack');
var combineLoaders = require('webpack-combine-loaders');

module.exports = {
  entry: './static/app/src/main.js',
  output: { path: __dirname + '/static/app/src/dist/', filename: 'bundle.js' },
  module: {
    loaders: [
      {
        test: /.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        query: {
          presets: ['es2015', 'react'],
          plugins: [
            ["transform-decorators-legacy"],
          ]
        }
      },
      {
        test: /\.css$/,
        loader: combineLoaders([
          {
            loader: 'style-loader'
          }, {
            loader: 'css-loader',
            query: {
              modules: true,
              localIdentName: '[name]__[local]___[hash:base64:5]'
            }
          }
        ])
      },
      {
          test: /\.scss$/,
          loaders: [ 'style', 'css?sourceMap', 'sass?sourceMap' ]
      }
    ]
  },
};

console.log("Ouputing to: " + __dirname + '/static/app/src/dist/')