from flask import Flask, render_template
from datetime import datetime
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()
    user = {'username': 'Роман'}
    if now.hour > 5 and now.hour < 12:
        time_of_day = "morning"
    elif now.hour >= 12 and now.hour < 17:
        time_of_day = "day"
    elif now.hour >= 17 and now.hour < 23:
        time_of_day = "evening"
    items = ["один", "два", "три", "четыре", "пять"]
    return render_template('index.html', title='Home', user=user, time_of_day=time_of_day, items=items)

@app.route("/simple")
def simple():
    a = request.args.get("a", default=1, type=float)
    b = request.args.get("b", default=2) 
    return f"<h1>{a}+{b}={a+b}</h1>"

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

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    a = request.form.get("a", default=0, type=float)
    b = request.form.get("b", default=0, type=float)
    print(a,b)
    return render_template("calc.html", a=a, b=b, result=a+b)