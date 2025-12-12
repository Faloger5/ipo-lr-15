from datetime import datetime
from app import app

# / — приветствие
@app.route("/")
def index():
    return "Добро пожаловать в Flask-приложение!"

# /hello/<name> — персональное приветствие
@app.route("/hello/<name>")
def hello(name):
    return f"Привет, {name}!"

# /square/<int:number> — квадрат числа
@app.route("/square/<int:number>")
def square(number):
    return f"Квадрат числа {number} равен {number ** 2}"

# Вариант 4: /time — текущее серверное время
@app.route("/time")
def time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Текущее серверное время: {now}"

# Вариант 4: /repeat/<word>/<n> — повторяет слово n раз
@app.route("/repeat/<word>/<int:n>")
def repeat(word, n):
    return f"Результат: {' '.join([word] * n)}"

