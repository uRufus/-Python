import json
import sqlite3

from framework.data_mapper import UserMapper, CategoryMapper, CourseMapper, CourseUserMapper
from framework.decorators import UrlDecorator
from framework.wsgi import Framework
from framework.url import Url
from framework.view import View
from framework.response import Response
from framework.templator import render
from framework.logger import Logger

logger = Logger
user = UserMapper(sqlite3.connect('framework/project_db'))
category = CategoryMapper(sqlite3.connect('framework/project_db'))
course = CourseMapper(sqlite3.connect('framework/project_db'))
course_user = CourseUserMapper(sqlite3.connect('framework/project_db'))

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
        categories = category.get_list()
        output = render('categories.html', request=request, object_list=categories, themes_list=UrlDecorator.urls)
        return Response(body=output)

    def post(self, request):
        for key, value in request.body.items():
            category.insert(value)
        return self.get(self, request)


@UrlDecorator('/courses', 'Courses')
class Courses(View):

    def get(self, request):
        courses = course.get_list()
        categories = category.get_list()
        output = render('courses.html', request=request, object_list=courses, categories=categories,
                        themes_list=UrlDecorator.urls)
        return Response(body=output)

    def post(self, request):
        course.insert((request.body['course'], request.body['category']))
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

        courses = course.get_list()
        output = render('assign_courses.html', request=request, object_list=courses, themes_list=UrlDecorator.urls)
        return Response(body=output)

    def post(self, request):
        for key, value in request.body.items():
            assign_courses = course_user.get_list_by_id(request.auth)
            cat = category.get_id_by_category(key)
            cour = course.get_id_by_category_id_name(cat[0], value)
            if cour not in assign_courses:
                course_user.insert((request.auth, cour[0]))
        return self.get(self, request)


app = Framework(UrlDecorator.urls)
