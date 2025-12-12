from flask import Flask # импортируем класс Flask из библиотеки flask
app = Flask(__name__) # создаём объект приложения Flask
from app import routes # подключаем файл routes.py, где описаны маршруты
