from pprint import pprint
from framework.request import Request
from framework.controller import control_func
from framework.view import View

# def application(environ, start_response):
#     """
#     :param environ: словарь данных от сервера
#     :param start_response: функция для ответа серверу
#     """
#     # pprint(environ)
#     request = Request(environ)
#     # print(request.method)
#     # print(request.path)
#     # print(request.headers)
#     # print(request.query_params)
#     # print(request.body)
#     # сначала в функцию start_response передаем код ответа и заголовки
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return control_func(request.method, request.path, request.body)



class Framework:

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
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
