from pprint import pprint
from framework.request import Request
from framework.view import View


class Framework:

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        pprint(environ)
        request = Request(environ)
        view = self._get_view(request)
        response = self._get_response(request, view)
        start_response(response.status, list(response.headers.items()))
        return [response.body.encode('UTF-8')]

    def _get_view(self, request: Request):
        path = request.path
        for url in self.urls:
            if url.path == path:
                return url.view
        return None

    def _get_response(self, request: Request, view: View):
        if hasattr(view, request.method):
            return getattr(view, request.method)(view, request)
        return ['Method is not supported']
