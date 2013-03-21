require.config {
	baseUrl: '/',

	urlArgs: 'v'+(Date.now()),

	config:
		'app':
			'fakeServer': false

	shim:
		'backbone':
			deps: ['jquery', 'underscore'],
			exports: 'Backbone'

		'underscore':
			exports: '_'

		'backbone.validation': ['backbone'],
		'backbone.routefilter': ['backbone'],
		'app': [
			'text',
			'backbone.validation',
			'bootstrap'
		]

	paths:
		'backbone': 'static/js_libs/backbone-min',
		'underscore': 'static/js_libs/underscore-min',
		'jquery': 'statuc/js_libs/jquery-1.9.1-min',

	packages: []
}