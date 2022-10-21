import numbers
from flask import Flask
from flask import render_template
from flask import request
from flask import abort
import person

app = Flask(__name__)

person1 = person.Person("Вася", 13)
person2 = person.Person("Петя", 14)
person3 = person.Person("Коля", 13)

persons = [person1, person2, person3]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/template")
def simple_template():
    name = request.args.get("name", default="user")
    numbers = [1, "some", 3, 9, 5]
    return render_template('index.html', title='Home', name=name , items=numbers)
@app.route('/form',  methods=['GET', 'POST'])
def form():
    a = request.form.get("a", default=0, type=float)
    b = request.form.get("b", default=0, type=float)
    res = a + b
    return render_template('form.html', res=res, a=a, b=b)
@app.route("/persons")
def persons_list():
    return render_template('persons.html', persons=persons)
@app.route("/persons/<id>")
def person_item(id):
    print("personID", id)
    id = int(id)
    if id > len(persons) or id <= 0:
        abort(404)
    person = persons[id-1]
    return render_template('person.html', person=person)
@app.route("/add", methods=['GET', 'POST'])
def persons_add():
    name = request.form.get("name")
    if name:
        age = request.form.get("age", default=0, type=float)
        description = request.form.get("description")
        p = person.Person(name, age, description)
        persons.append(p)
    return render_template('add_person.html')