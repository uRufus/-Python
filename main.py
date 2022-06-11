import json
import sqlite3

from framework.data_mapper import UserMapper
from framework.decorators import UrlDecorator
from framework.wsgi import Framework
from framework.url import Url
from framework.view import View
from framework.response import Response
from framework.templator import render
from framework.logger import Logger

logger = Logger
user = UserMapper(sqlite3.connect('framework/project_db'))


@UrlDecorator('/', 'Главная')
class MainPage(View):

    def get(self, request):
        output = render('index.html', request=request, themes_list=UrlDecorator.urls)
        logger._log_data('index_file', output)
        return Response(body=output)

    def post(self, request):
        output = render('index.html', request=request, themes_list=UrlDecorator.urls)
        logger._log_data('index_file', output)
        return Response(body=output)


@UrlDecorator('/about', 'О нас')
class About(View):

    def get(self, request):
        output = render('about.html', request=request, themes_list=UrlDecorator.urls)
        return Response(body=output)

    def post(self, request):
        output = render('about.html', request=request, themes_list=UrlDecorator.urls)
        return Response(body=output)


@UrlDecorator('/contacts', 'Контакты')
class Contacts(View):

    def get(self, request):
        output = render('contacts.html', request=request, themes_list=UrlDecorator.urls)
        logger._log_data('contacts', output)
        return Response(body=output)

    def post(self, request):
        try:
            with open(f'framework/mails/{request.body["theme"]}', mode='w+', encoding='utf-8') as f:
                for key, value in request.body.items():
                    f.write(f'{key}: {value}\n')
            return Response(status='201 Created', body='Your message was received')
        except KeyError:
            output = render('contacts.html', request=request, themes_list=UrlDecorator.urls)
            return Response(body=output)


@UrlDecorator('/categories', 'Categories')
class Categories(View):

    def get(self, request):
        categories = []
        with open('framework/file_db/categories', mode='r', encoding='utf-8') as f:
            for value in f.readlines():
                categories.append(value)
        output = render('categories.html', request=request, object_list=categories, themes_list=UrlDecorator.urls)
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
        output = render('courses.html', request=request, object_list=courses, themes_list=UrlDecorator.urls)
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


@UrlDecorator('/registration', 'Registration')
class Registration(View):

    def get(self, request, message=None):
        output = render('registration.html', request=request, message=message, themes_list=UrlDecorator.urls)
        return Response(body=output)

    def post(self, request):
        try:
            if request.body['login']:
                key, value = request.body.values()
                if user.find_by_login(key):
                    message = 'The user already exists'
                else:
                    user.insert({key: value})
                    message = 'The user was created'
            return self.get(self, request, message)
        except KeyError:
            return self.get(self, request)


@UrlDecorator('/students_list', 'Students')
class Students(View):

    def get(self, request):
        students = user.get_list()
        output = render('students_list.html', request=request, students=students, themes_list=UrlDecorator.urls)
        return Response(body=output)

    def post(self, request):
        students = user.get_list()
        output = render('students_list.html', request=request, students=students, themes_list=UrlDecorator.urls)
        return Response(body=output)


@UrlDecorator('/assign_courses', 'AssignCourses')
class AssignCourses(View):

    def get(self, request):
        with open('framework/file_db/courses.json', mode='r') as f:
            courses = json.load(f)
        output = render('assign_courses.html', request=request, object_list=courses, themes_list=UrlDecorator.urls)
        return Response(body=output)

    def post(self, request):
        with open('framework/file_db/assign_courses.json', mode='r') as f:
            assign_courses = json.load(f)
        with open('framework/file_db/assign_courses.json', mode='w') as f:
            for key, value in request.body.items():
                if request.auth in assign_courses:
                    if key in assign_courses[request.auth]:
                        if value not in assign_courses[request.auth][key]:
                            assign_courses[request.auth][key].append(value)
                    else:
                        assign_courses[request.auth][key] = [value]
                else:
                    assign_courses[request.auth] = {key: [value]}
                logger._log_data(log=assign_courses, writen_method='console')
                json.dump(assign_courses, f)
        return self.get(self, request)

app = Framework(UrlDecorator.urls)
