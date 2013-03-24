define (require, exports, module) ->

	# Packages loading
	index = require 'index'

	#Utils and other
	Utils = require 'shared/utils'

	exports.App = Backbone.Router.extend {
		routes:
			'*other': 'unknownRoute'

		initialize: ->
			Utils.bindRoutes @, [
				index.Controller
			]

		unknownRoute: ->
			console.log 'unknown route'
	}
	return