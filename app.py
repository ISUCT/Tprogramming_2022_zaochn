from unicodedata import name
from flask import Flask
from datetime import datetime
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()
    user = {'username': 'Alex'}
    if now.hour > 6 and now.hour < 12:
        time_of_day = "morning"
    elif now.hour >= 12 and now.hour < 17:
        time_of_day = "day"
    elif now.hour >= 17 and now.hour < 23:
        time_of_day = "evening"
    items = ["one", "two", "three", "four", "five"]

    return render_template('index.html',
    title='Home',
    user=user,
    time_of_day=time_of_day,
    items=items)

# http://127.0.0.1:5000/calculator?a=5&some=10&b=hello -- передаем некие параметры
@app.route("/calculator")
def calculator():
    a = request.args.get("a", default=0, type=float)
    b = request.args.get("b", default=0, type=float)
    return f"<h1>{a}+{b}={a+b}</h1>"

@app.route("/hello")
def hello_world():
    now = datetime.now()
    return f"<p>Hello, World! {now}</p>"

@app.route("/styled")
def hello_styles():
    now = datetime.now()
    return f"""
    <h1>Header</h1>
    <p>Hello, World!</p>
    <p>Real time {now} 
    """

# рабочий калькулятор через POST запрос
@app.route("/calculator_ok", methods = ['GET', 'POST'])
def calculator_ok():
    a = request.form.get("a", default = 0, type = float)
    b = request.form.get("b", default = 0, type = float)
    return render_template("calculator_ok.html", a=a, b=b, result = a+b)

import cat

cats = {
    "vasya": cat.Cat("vasya", 3),
    "barsik": cat.Cat("barsik", 1),
    "murzik": cat.Cat("murzik", 5),
}

@app.route("/cats")
def list_cats():
    return render_template("cats.html", cats = cats)

@app.route("/cats/<name>")
def list_link_cats(name):
    cat = cats[name]
    return render_template("cat.html", cat = cat)

# добавляем нового кота (после ребута сервера новые коты пропадут)
@app.route("/cats/new", methods = ["GET", "POST"])
def create_cats():
    name = request.form.get("name", default = "")
    age = request.form.get("age", default = 0, type = float)
    if name:
        new_cat = cat.Cat(name, age)
        cats[new_cat.name] = new_cat
    return render_template("new_cat.html")

