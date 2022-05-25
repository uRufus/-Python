from framework.wsgi import Framework
from framework.url import Url
from framework.view import View
from framework.response import Response



class MyFirstView(View):

    def get(self, request):
        return Response(body='GET SUCCESS')

    def post(self, request):
        return Response(status='201 Created', body='POST SUCCESS', headers={'Babayka': '123'})

urls = [
    Url('/homepage', MyFirstView)
]

app = Framework(urls)
