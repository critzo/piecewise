require('dotenv').config({path: '../.env'})
require("babel-polyfill");

const path = require('path');
const webpack = require('webpack');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const HtmlWebpackHarddiskPlugin = require('html-webpack-harddisk-plugin');

module.exports = env => {

  console.log('NODE_ENV: ', process.env.PIECEWISE_ENV);

  return {
    module: {
      rules: [
        {
          test: /\.worker\.js$/,
          use: { loader: 'worker-loader' }
        },
        {
          test: /\.(s*)css$/i,
          use: [
            {loader: 'style-loader'},
            {loader: MiniCssExtractPlugin.loader},
            {loader: 'css-loader'},
            {
              loader: 'postcss-loader',
              options: {
                plugins: function () {
                  return [
                    require('precss'),
                    require('autoprefixer')
                  ];
                }
              }
            },
            {loader: 'sass-loader'}
          ],
        },
        {
          test: /\.m?js$/,
          exclude: /(node_modules|bower_components)/,
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env']
          }
        },
        {
          test: /\.(png|svg|jpg|gif)$/,
          loader: 'file-loader',
          options: {
            esModule: false,
          }
        },
        {
          test: /\.html$/,
          loader: 'html-loader'
        }
      ]
    },
    entry: [
      "babel-polyfill",
      './static/js/index.js'
    ],
    output: {
      filename: 'main.js',
      path: path.resolve(__dirname, 'dist'),
    },
    plugins: [
      new MiniCssExtractPlugin(),
      new HtmlWebpackPlugin({
        alwaysWriteToDisk: true,
        template: path.resolve(__dirname, 'templates/index.html'),
        filename: 'index.html',
        inject: true
      }),
      new HtmlWebpackPlugin({
        template: path.resolve(__dirname, 'templates/form.html'),
        filename: 'form.html',
      }),
      new HtmlWebpackHarddiskPlugin(),
      // new webpack.EnvironmentPlugin([
      //   'PIECEWISE_BACKEND_URL'
      // ])
    ],
    devServer: {
      contentBase: path.resolve(__dirname, "dist"),
      index: "./templates/index.html"
    }
  }
};
