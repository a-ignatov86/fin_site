Шаблон сайта волонтеров по финансовой грамотности

1) django-admin startprogect name создаем проект
2) создаем приложение hello_app manage.py startapp hello_app (блок в джано проекте)
3) добавляем приложение в settings.py INSTALLED APP
4) добавляем шаблон в settings.py TEMPLATES папка Templates - фронтенд нашего проекта, в settings TEMPLATES прописываем ключ-значение 'DIRS': ['templates'],
5) в views.py приложения прописывем функцию response -> отправляем нашу начальную страницу на запрос
6) urls.py связь URL И views def







manage.py -- запускает сервер проекты

folderForWebSite
settings.py -- хранит пароли, структуру приложения
urls.py - хранит адреса страниц и передает во views

folderForApp
models.py -- for reletions whith sqlite
views.py -- соединяет templates & SQL


templates -- папка с html и css (фронтенд)