define (require, exports, module) ->

	Model = require('./models')

	exports.News = class NewsCollection extends Backbone.Collection
		url: "/news/"
		model: Model.News

		parse: (response) ->
			console.log response
			response.news

	return