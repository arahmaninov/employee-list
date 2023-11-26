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

@app.route("/addemployee", methods = ["POST", "GET"])
def add_employee():
    if request.method == "POST":
        try:
            lastname = request.form["lastname"]
            name = request.form["name"]
            surname = request.form["surname"]
            date = request.form["date"]
            position = request.form["position"]

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO employee (lastname, name, surname, date, position) VALUES (?, ?, ?, ?, ?)", (lastname, name, surname, date, position))

                con.commit()
                status = "Запись успешно добавлена"
        except:
            con.rollback()
            status = "Ошибка при добавлении записи"

        finally:
            con.close()
            return render_template("result.html", status=status)
