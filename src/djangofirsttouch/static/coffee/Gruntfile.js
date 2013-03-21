module.exports = function(grunt) {
    grunt.initConfig({

        coffee: {
            options: {
                bare: true
            },
            glob_to_multiple: {
                expand: true,
                cwd: './src/',
                src: [
                    '*.coffee',
                    '**/*.coffee'
                ],
                dest: '../js',
                ext: '.js'
            }
        },

        watch: {
            files: [
                'src/*.coffee',
                'src/**/*.coffee'
            ],
            tasks: ['coffee']
        }

    });
    grunt.loadNpmTasks('grunt-contrib-coffee');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Setup tasks, wanch should be last
    grunt.registerTask('run', ['coffee', 'watch']);
    grunt.registerTask('default', ['run']);
};