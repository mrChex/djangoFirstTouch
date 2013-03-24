define (require, exports, module)->
	exports.News = class NewsModel extends Backbone.Model
		defaults:
			title: ""
			text: ""


	return