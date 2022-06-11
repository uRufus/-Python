# -Python
Архитектура и шаблоны проектирования на Python

To start wsgi you need to type in terminal the following command:
gunicorn main:app -b:8001

main.py - start framework. Get URL to framework
url.py - Url dataclass to form proper url (path, view)
view.py - class View(template) with get|post methods
wsgi.py - Framework with request/ response
request.py - getting params form request
response.py - forming response 
templator.py - rendering web page
decorators.py - place to create decorators. UrlDecorator is used to map url, view and page's title

1. Добавить базу данных к своему проекту
2. Для этого использовать паттерн Data Mapper
3. Использовать паттерн Unit of Work
4. Можно попробовать дополнительно реализовать Identity Map