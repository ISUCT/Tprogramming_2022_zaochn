from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route("/")
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