var webpack = require('webpack');
module.exports = {
  entry: [
    "./diagnoser/static/es6/diagnoser.js"
  ],
  output: {
    path: __dirname + '/diagnoser/static',
    filename: "bundle.js"
  },
  module: {
    loaders: [
      {
        test: /\.js?$/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015', 'react']
        },
        exclude: /node_modules/
      }
    ]
  },
  plugins: [
  ]
};