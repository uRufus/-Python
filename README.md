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

