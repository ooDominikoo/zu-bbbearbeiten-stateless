import helper
from flask import Flask, request, Response, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/") #Definiert, auf welche URLs reagiert wird
def index():
    todos = helper.get_all()
    return render_template('index.html', todos=todos) #Daten an index.html übergeben


@app.route('/add', methods=["POST"])    #Definiert, auf welche URLs reagiert wird
def add():
    title = request.form.get("title")
    helper.add(title)
    return redirect(url_for("index"))


@app.route('/update/<int:index>')   #Definiert, auf welche URLs reagiert wird
def update(index):
    helper.update(index)
    return redirect(url_for("index"))