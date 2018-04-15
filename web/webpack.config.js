const webpack = require('webpack');
const NODE_ENV = process.env.NODE_ENV || 'development';
const BundleTracker =  require('webpack-bundle-tracker');


module.exports = {
    mode: NODE_ENV,
    node: {
        __dirname: true
    },

    context: __dirname + "/static_src",
    entry: {
        index: './index.js'
    },
    output: {
        path: `${__dirname}/static/build`,
        // path: __dirname + "/static/build",
        filename: "[name].js",
        library: "[name]"
    },



    watch: NODE_ENV == 'development',
    watchOptions: {
        aggregateTimeout: 100
    },
    devtool: "cheap-inline-module-source-map",

    plugins: [
        new webpack.NoEmitOnErrorsPlugin(),
        new webpack.NodeEnvironmentPlugin('NODE_ENV'),
        new BundleTracker()
    ],


    module: {
        rules: [{
            test: /(\.js$)|(\.jsx$)/,
            use: {
                loader: 'babel-loader'
            }
        }]
    }
};


// if (NODE_ENV == 'production') {
//     module.exports.plugins.push(
//         new webpack.optimize.UglifyJSPlugin()
//     )
// }