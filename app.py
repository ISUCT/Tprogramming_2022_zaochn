from crypt import methods
from flask import Flask, render_template
from datetime import datetime
from flask import request

import cat

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()
    user = {'username': 'Сергей'}
    if now.hour > 5 and now.hour < 12:
        time_of_day = "morning"
    elif now.hour >= 12 and now.hour < 17:
        time_of_day = "day"
    elif now.hour >= 17 and now.hour < 23:
        time_of_day = "evening"
    items = ["один", "два", "три", "четыре", "пять"]
    return render_template('index.html', 
                            title='Home', 
                            user=user, 
                            time_of_day=time_of_day,
                            items=items)

@app.route("/simple")
def simple():
    a = request.args.get('a', default=0, type=float)
    b = request.args.get('b', default=0, type=float)
    return f'<h1>{a}+{b}={a+b}</h1>'

@app.route("/hello")
def hello_world():
    now = datetime.now()
    return f"<p>Hello, World! {now}</p>"

@app.route("/styled")
def hello_styles():
    now = datetime.now()
    return f"""
    <h1>Заголовок</h1>
    <p>hello_world!</p>
    <p>Текущее время {now} </p>
    """

@app.route('/calc', methods =['GET', 'POST'])
def calc():
    a = request.form.get("a", default = 0, type = float)
    b = request.form.get("b", default = 0, type = float)
    return render_template("calc.html", a=a, b=b, result=a+b)

cats = {
    "vasya": cat.Cat("vasya", 3),
    "barsik": cat.Cat("barsik", 3),
    "murzik": cat.Cat("murzik", 3), 
}

@app.route('/cats')
def list_cats():
    return render_template("cats.html", cats = cats)

@app.route("/cats/<name>")
def show_cat(name):
    cat = cats[name]
    return render_template("cat.html", cat = cat)

@app.route("/cats/new", methods=["GET", "POST"])
def create_cat():
    name = request.form.get("name",default="untitled")
    age = request.form.get("age",default=0,type=float)
    
    new_cat = cat.Cat(name, age)

    cats[new_cat.name] = new_cat

    return render_template("new_cat.html")
