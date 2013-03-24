console.log "Loading require config"
require.config
	baseUrl: '/static/js/'

	urlArgs: 'v'+(Date.now())

	config:
		app:
			fakeServer: false

	shim:
		backbone:
			deps: ['jquery', 'underscore']
			exports: 'Backbone'

		bootstrap:
			deps: ['jquery']
			exports: 'Bootstrap'

		underscore:
			exports: '_'

		'backbone.validation': ['backbone']
		'backbone.routefilter': ['backbone']
		app: [
			'backbone'
			'underscore'
			'bootstrap'
		]

	paths:
		backbone: '/static/js_libs/backbone-min'
		bootstrap: '/static/js_libs/bootstrap.min'
		underscore: '/static/js_libs/underscore-min'
		jquery: '/static/js_libs/jquery-1.9.1.min'
		text: '/static/js_libs/text'
		app: '/static/js/app'

	packages: ['index']
