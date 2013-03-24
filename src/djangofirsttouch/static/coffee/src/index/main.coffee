define (require, exports, module)->
	View = require './view'
	Collection = require './collections'

	BaseController = require 'shared/base_controller'

	exports.Controller = class Controller extends BaseController
		routes:
			'': 'index'

		index: ->
			@indexView = new View.View
				CollectionNews: new Collection.News()

			$('#index-box').html @indexView.render().$el
			return @

	return