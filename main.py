from framework.wsgi import Framework
from framework.url import Url
from framework.view import View
from framework.response import Response
from framework.templator import render


class MainPage(View):

    def get(self, request):
        output = render('index.html', object_list='GET SUCCESS')
        return Response(body=output)

    def post(self, request):
        return Response(status='201 Created', body='POST SUCCESS')

class About(View):

    def get(self, request):
        output = render('about.html', object_list='GET SUCCESS')
        return Response(body=output)

    def post(self, request):
        return Response(status='201 Created', body='POST SUCCESS')

class Contacts(View):

    def get(self, request):
        output = render('contacts.html', object_list='GET SUCCESS')
        return Response(body=output)

    def post(self, request):
        with open(f'framework/mails/{request.body["theme"]}', mode='w+', encoding='utf-8') as f:
            for key, value in request.body.items():
                f.write(f'{key}: {value}\n')
        return Response(status='201 Created', body='Your message was received')

urls = [
    Url('/index', MainPage),
    Url('/about', About),
    Url('/contacts', Contacts),
]

app = Framework(urls)
