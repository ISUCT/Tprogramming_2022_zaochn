from flask import Flask
from datetime import datetime
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()
    user = {"username": 'Mihail'}
    if now.hour > 5 and now.hour < 12:
        time_of_day = "morning"
    elif now.hour >= 12 and now.hour < 17:
        time_of_day = "day"
    elif now.hour >= 17 and now.hour < 23:
        time_of_day = "evening"
    items = ["один", "два", "три", "четыре", "пять"]    

    return render_template('index.html', 
    titel='Home',
    user=user, 
    time_of_day=time_of_day,
    items=items)
    

@app.route("/simple")
def simple():
    a = request.args.get("a", default=0,type=float)
    b = request.args.get("b", type=float)
    return f"<h1>{a}+{b}={a+b}</h1>"

@app.route("/")
def hello_world():
    now = datetime.now()
    return f"<p>Hello, World!{now}</p>"

@app.route("/styled")
def hello_styles():
    now = datetime.now()
    return f"""
    <h1>Заголовок</h1>
    <p>Hello, World!</p>"
    <p>Текущее время{now}</p>
    """

@app.route("/calc", methods=['GET', 'POST'])
def calc():
    a = request.form.get("a", default=0, type=float)
    b = request.form.get("b", default=0, type=float)
    return render_template("calc.html", a=a, b=b, result = a+b) 

import cat
cats = {
        "vasya":  cat.Cat("vasya", 5),
        "barsik": cat.Cat("barsik", 3),
        "murzik": cat.Cat("murzik", 3),
    }
@app.route("/cats")
def list_cats():
    return render_template("cats.html", cats = cats)

@app.route("/cats/<name>")
def fish(name):
     cat = cats[name]
     return render_template("cat.html", cat = cat)

@app.route("/cats/new", methods=["GET", "POST"])
def create_cat():
    name = request.form.get("name",default="untiled")
    age = request.form.get("age", default=0, type=float)
    if name:
       new_cat = cat.Cat(name, age)
       cats[new_cat.name] = new_cat
    return render_template("new_cat.html")
