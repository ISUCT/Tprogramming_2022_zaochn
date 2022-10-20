from typing import ItemsView
from flask import Flask
from flask import request
from flask import render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Время {datetime.now()}</p>"

@app.route("/sample", methods=['GET', 'POST'])
def sample():
    a = request.form.get("a", default=0, type=float)
    b = request.form.get("b", default=0, type=float)
    res = a + b
    items = ["один", "два", "три", "четыре", "пять"]
    name = request.args.get("name", default="user")
    return render_template('index.html', title='Home', name=name, items=items, a=a, b=b, res=res)
