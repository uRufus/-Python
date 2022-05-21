
class Request:

    def __init__(self, environ):
        self.method = environ.get('REQUEST_METHOD')
        self.path = environ.get('PATH_INFO')
        self.headers = self._get_headers(environ)
        self.query_strings = self._get_query_strings(environ)
        self.body = self._get_body(environ)

    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                headers[key[5:].lower()] = value
        return headers

    def _get_query_strings(self, environ):
        queries = {}
        for key, value in environ.items():
            if key.startswith('QUERY_STRING'):
                queries[key.lower()] = value
        return queries

    def _get_body(self, environ):
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        return environ['wsgi.input'].read(request_body_size).decode('UTF-8')
