

from framework.url import Url


class UrlDecorator:
	urls = []

	def __init__(self, path, title):
		self.path = path
		self.title = title

	def __call__(self, view):
		self.urls.append(Url(self.path, view, self.title))


