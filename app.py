import cat
from flask import Flask
from datetime import datetime
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    user = {'username': 'Egor'}
    now = datetime.now()

    if now.hour > 5 and now.hour < 12:
        timeOfDay = 'morning'

    elif now.hour >= 12 and now.hour < 17:
        timeOfDay = 'day'

    elif now.hour >= 17 and now.hour < 23:
        timeOfDay = 'evening'

    items = ['один', 'два', 'три', 'четыре', 'пять']

    return render_template('index.html',
                           title='Home',
                           user=user,
                           timeOfDay=timeOfDay,
                           items=items)


@app.route('/simple')
def simple():

    a = request.args.get('a', default=0, type=float)
    b = request.args.get('b', default=0, type=float)

    return f'<h1>{a} + {b} = {a + b}</h1>'


@app.route("/hello")
def hello_world():

    now = datetime.now()

    return f"<p>Hello, World! {now}</p>"


@app.route("/styled")
def hello_styles():

    now = datetime.now()

    return f"""
            <h1>ЗаГоЛоВоК</h1>
            <p>Hello, World</P>
            <p>Текущее время {now}</p>
     """


@app.route('/calc', methods=['GET', 'POST'])
def calc():

    a = request.form.get('a', default=0, type=float)
    b = request.form.get('b', default=0, type=float)

    return render_template('calc.html',
                           a=a,
                           b=b,
                           result=a + b)


cats = {
    'vasya': cat.Cat('vasya', 3),
    'petya': cat.Cat('petya', 7),
    'barsik': cat.Cat('barsik', 4),
    'venom': cat.Cat('venom', 8),
    'gosha': cat.Cat('gosha', 5)
}


@app.route('/cats')
def list_cats():
    return render_template('cats.html', cats=cats)


@app.route('/cats/<name>')
def show_cat(name):
    cat = cats[name]
    return render_template('cat.html', cat=cat)


@app.route('/cats/new', methods=['GET', 'POST'])
def create_cat():

    name = request.form.get('name', default='untitled')
    age = request.form.get('age', default=0, type=float)
    if name:
        newCat = cat.Cat(name, age)
        cats[newCat.name] = newCat

    return render_template('newCat.html')
