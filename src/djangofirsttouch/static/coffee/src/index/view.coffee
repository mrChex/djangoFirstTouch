define (require, exports, module) ->
	tpl = require 'text!/static/coffee/src/index/templates/index.html'

	BaseView = require 'shared/base_view'

	exports.View = class MyView extends BaseView
		template: _.template tpl

#		events:
#			'click #demo-open': 'showNotification'

		initialize: (CollectionNews)->
			@CollectionNews = CollectionNews.CollectionNews

		render: =>
			@$el.html "Loading..."
			console.log @CollectionNews
			@CollectionNews.fetch
				success: =>
					@$el.html @template
						news: @CollectionNews.models
				error: ->
					console.log "Error"
					console.log arguments

			return @


	return