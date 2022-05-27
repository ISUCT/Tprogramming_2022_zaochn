from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    now = datetime.now()
    return f"<p>Hello, World! {now} </p>"