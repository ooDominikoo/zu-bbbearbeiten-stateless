import helper

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")  # Definiert, auf welche URLs reagiert wird
def index():
    todos = helper.get_all()
    return render_template("index.html", todos=todos)
    # Daten an index.html übergeben


# Definiert, auf welche URLs reagiert wird
@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    date = request.form.get("date")
    helper.add(title, date)
    return redirect(url_for("index"))


# Definiert, auf welche URLs reagiert wird
@app.route("/update/<int:index>")
def update(index):
    helper.update(index)
    return redirect(url_for("index"))
