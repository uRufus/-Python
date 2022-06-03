import json

from framework.decorators import UrlDecorator
from framework.wsgi import Framework
from framework.url import Url
from framework.view import View
from framework.response import Response
from framework.templator import render
from framework.logger import Logger

logger = Logger


@UrlDecorator('/', 'Главная')
class MainPage(View):

    def get(self, request):
        output = render('index.html', object_list='GET SUCCESS', themes_list=UrlDecorator.urls)
        logger._log_data('index_file', output)
        return Response(body=output)

    def post(self, request):
        return Response(status='201 Created', body='POST SUCCESS')


@UrlDecorator('/about', 'О нас')
class About(View):

    def get(self, request):
        output = render('about.html', object_list='GET SUCCESS', themes_list=UrlDecorator.urls)
        return Response(body=output)

    def post(self, request):
        return Response(status='201 Created', body='POST SUCCESS')


@UrlDecorator('/contacts', 'Контакты')
class Contacts(View):

    def get(self, request):
        output = render('contacts.html', object_list='GET SUCCESS', themes_list=UrlDecorator.urls)
        logger._log_data('contacts', output)
        return Response(body=output)

    def post(self, request):
        with open(f'framework/mails/{request.body["theme"]}', mode='w+', encoding='utf-8') as f:
            for key, value in request.body.items():
                f.write(f'{key}: {value}\n')
        return Response(status='201 Created', body='Your message was received')


@UrlDecorator('/categories', 'Categories')
class Categories(View):

    def get(self, request):
        categories = []
        with open('framework/file_db/categories', mode='r', encoding='utf-8') as f:
            for value in f.readlines():
                categories.append(value)
        output = render('categories.html', object_list=categories, themes_list=UrlDecorator.urls)
        return Response(body=output)

    def post(self, request):
        with open('framework/file_db/categories', mode='a', encoding='utf-8') as f:
            for key, value in request.body.items():
                f.write(f'\n{value}')
        return self.get(self, request)


@UrlDecorator('/courses', 'Courses')
class Courses(View):

    def get(self, request):
        with open('framework/file_db/courses.json', mode='r') as f:
            courses = json.load(f)
        output = render('courses.html', object_list=courses, themes_list=UrlDecorator.urls)
        return Response(body=output)

    def post(self, request):
        with open('framework/file_db/courses.json', mode='r') as f:
            courses = json.load(f)
        with open('framework/file_db/courses.json', mode='w') as f:
            key, value = request.body.values()
            if key in courses:
                courses[key].append(value)
            else:
                courses[key] = [value]
            print(courses)
            json.dump(courses, f)
        return self.get(self, request)

# urls = [
#     Url('/', MainPage, 'Главная'),
#     Url('/about', About, 'О нас'),
#     Url('/contacts', Contacts, 'Контакты'),
#     Url('/categories', Categories, 'Categories'),
#     Url('/courses', Courses, 'Courses'),
# ]

app = Framework(UrlDecorator.urls)
