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

we need to assign template to view 

0. Добавить в свой wsgi-фреймворк возможность обработки post-запроса +
1. Добавить в свой wsgi-фреймворк возможность получения данных из post запроса +
2. Дополнительно можно добавить возможность получения данных из get запроса +
3. В проект добавить страницу контактов на которой пользователь может отправить нам сообщение (пользователь вводит тему сообщения, его текст, свой email)
4. После отправки реализовать сохранение сообщения в файл, либо вывести сообщение в терминал (базу данных пока не используем)