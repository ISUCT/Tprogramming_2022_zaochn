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
    user = {'username': 'Павлик'}
    return render_template('index.html', title='home', user=user)

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