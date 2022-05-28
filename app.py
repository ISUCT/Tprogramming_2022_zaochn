from turtle import title
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
from flask import Flask
from datetime import datetime
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()
    user = {'username': 'Павлик'}
    if now.hour > 5 and now.hour < 12:
        time_of_day = "morning"
    elif now.hour >= 12 and now.hour < 17:
        time_of_day = "day"
    elif now.hour >= 17 and now.hour < 23:
        time_of_day = "evening"
    items = ["один", "два", "три", "четыре", "пять"]

    return render_template('index.html', title='home', user=user, time_of_day=time_of_day, items=items, )

@app.route("/Hello")
def hello_world():
    now = datetime.now()
    return f"<p>О ПРЕКРАСНЫЙ СУП НАВАРИЛИ! {now}</p>"

@app.route("/styled")
def hello_styles():
    now = datetime.now()
    return f"""
    <h1>Заголовушка</h1>
    <p>О ПРЕКРАСНЫЙ СУП НАВАРИЛИ!</p>
    <p>Времы судного дня {now}</p>
    """