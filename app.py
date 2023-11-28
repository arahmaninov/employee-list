from flask import Flask, render_template, request
import sqlite3
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.sql import text
#import os.path

#db = SQLAlchemy()

app = Flask(__name__)

#db_name = 'database.db'

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#db_path = os.path.join(BASE_DIR, db_name)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#db.init_app(app)

#class Employee(db.Model):
#    __tablename__ = 'employee'
#    lastname = db.Column(db.String, primary_key=True)
#    name = db.Column(db.String)
#    surname = db.Column(db.String)
#    date = db.Column(db.String)
#    position = db.Column(db.String)

#class Position(db.Model):
#    __tablename__ = 'position'
#    title = db.Column(db.String, primary_key=True)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/employees")
def show_employees():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT rowid, * FROM employee")

    rows = cur.fetchall()
    con.close()

    return render_template("employees.html", rows=rows)

    #try:
    #    rows = db.session.execute(db.select(Position)).scalars()
    #    return render_template("employees.html", rows=rows)
    #except Exception as e:
    #    error_text = "<p>The error:<br>" + str(e) + "</p>"
    #    hed = '<h1>Something is broken.</h1>'
    #    return hed + error_text


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

@app.route("/editemployee", methods=["POST", "GET"])
def edit_employee():
    if request.method == "POST":
        try:
            id = request.form["id"]

            con = sqlite3.connect("database.db")
            con.row_factory = sqlite3.Row
            
            cur = con.cursor()
            print("Test before select operation")
            cur.execute("SELECT rowid, * FROM employee WHERE rowid = ?", (id))

            rows = cur.fetchall()
            
            print("Rows:", rows)
            print("It should work here except it doesn't") 
        except:
            id=None
            print("Here is our exception:", lastnameid)
        finally:
            con.close()
            return render_template("editemployee.html", rows=rows)

@app.route("/edit", methods=["POST", "GET"])
def employeeedited():
    if request.method == "POST":
        try:
            rowid = request.form["rowid"]
            lastname = request.form["lastname"]
            name = request.form["name"]
            surname = request.form["surname"]
            date = request.form["date"]
            #position = request.form["position"]

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                print("It seems to work until here")
                cur.execute("UPDATE employees SET lastname='"+lastname+"' WHERE rowid= ?", (rowid))
                print("Update successful")
                con.commit()
                print("Commit successful")
                status = "Запись успешно обновлена"
        except:
            con.rollback()
            status = "Ошибка при обновлении записи"

        finally:
            con.close()
            return render_template("result.html", status=status)
