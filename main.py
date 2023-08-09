from flask import *
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html");

@app.route("/add")
def add():   
    return render_template("add.html")

@app.route("/savedetails",methods = ["POST","GET"])
def saveDetails():
    message = "message"
    if request.method == "POST":
        try:
            name = request.form["name"]
            address = request.form["address"]
            city = request.form["city"]
            pincode = request.form["pincode"]
            mobile = request.form["mobile"]
            email = request.form["email"]
            with sqlite3.connect("addressbook.db") as connection:
                cursor = connection.cursor()   
                cursor.execute("INSERT into Address (name, address, city, pincode, mobile, email) values (?,?,?,?,?,?)",(name,address,city,pincode,mobile,email))
                connection.commit()
                message = "Success! Contact successfully Added."   
        except:
            connection.rollback()
            message = "Error! Something went to wrong."
        finally:
            return render_template("success.html", message=message)
            connection.close()

@app.route("/view")
def view():
    connection = sqlite3.connect("addressbook.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("select * from Address")   
    rows = cursor.fetchall()
    return render_template("view.html",rows = rows)

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deleterecord",methods = ["POST"])   
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("addressbook.db") as connection:
        try:
            cursor = connection.cursor()
            cursor.execute("delete from Address where id = ?",id)
            message = "Success! Contact successfully deleted"   
        except:
            message = "Error! Can't be Deleted"
        finally:
            return render_template("deleterecord.html",message = message)

if __name__ == "__main__":
    app.run(debug = True)  
