module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        uglify: {
            dist: {
                files: {
                    'lib/jsqrcode-combined.min.js': [
                        "restaurantp/manejo_pedidos/templates/js/grid.js",
                        "restaurantp/manejo_pedidos/templates/js/version.js",
                        "restaurantp/manejo_pedidos/templates/js/detector.js",
                        "restaurantp/manejo_pedidos/templates/js/formatinf.js",
                        "restaurantp/manejo_pedidos/templates/js/errorlevel.js",
                        "restaurantp/manejo_pedidos/templates/js/bitmat.js",
                        "restaurantp/manejo_pedidos/templates/js/datablock.js",
                        "restaurantp/manejo_pedidos/templates/js/bmparser.js",
                        "restaurantp/manejo_pedidos/templates/js/datamask.js",
                        "restaurantp/manejo_pedidos/templates/js/rsdecoder.js",
                        "restaurantp/manejo_pedidos/templates/js/gf256poly.js",
                        "restaurantp/manejo_pedidos/templates/js/gf256.js",
                        "restaurantp/manejo_pedidos/templates/js/decoder.js",
                        "restaurantp/manejo_pedidos/templates/js/qrcode.js",
                        "restaurantp/manejo_pedidos/templates/js/findpat.js",
                        "restaurantp/manejo_pedidos/templates/js/alignpat.js",
                        "restaurantp/manejo_pedidos/templates/js/databr.js",
                    ],
                    'lib/html5-qrcode.min.js': ['restaurantp/manejo_pedidos/html5-qrcode.js']
                },
                options: {
                    beautify: false,
                    mangle: false,
                    sourceMap: false
                }
            }
        },
        watch: {
            js: {
                files: ['src/*.js']
            }
        }
    });

    // Load the plugin that provides the tasks.
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task(s).
    grunt.registerTask('default', [
        'uglify'
    ]);
};