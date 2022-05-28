class Request:

    def __init__(self, environ):
        self.method = environ.get('REQUEST_METHOD').lower()
        self.path = environ.get('PATH_INFO')
        self.headers = self._get_headers(environ)
        self.query_params = self._get_query_params(environ)
        self.body = self._get_body(environ)

    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                headers[key[5:].lower()] = value
        return headers

    def _get_query_params(self, environ):
        query_params = {}
        qs = environ.get('QUERY_STRING')

        if not qs:
            return {}

        qs = qs.split('&')
        for q_str in qs:
            key, value = q_str.split('=')
            if query_params.get(key):
                query_params[key].append(value)
            else:
                query_params[key] = [value]
        return query_params

    def _get_body(self, environ):
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except ValueError:
            request_body_size = 0
        return environ['wsgi.input'].read(request_body_size).decode('UTF-8')

