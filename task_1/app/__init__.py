from flask import Flask

app = Flask(__name__)

# подключаем маршруты
from app import routes
