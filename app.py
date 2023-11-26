from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/employees")
def show_employees():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM employee")

    rows = cur.fetchall()
    con.close()

    return render_template("employees.html", rows=rows)

@app.route("/newemployee")
def new_employee():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM position ORDER BY title")

    rows = cur.fetchall()
    con.close()

    return render_template("newemployee.html", rows=rows)
