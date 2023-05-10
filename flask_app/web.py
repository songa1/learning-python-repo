#!/usr/bin/python3

from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import csv

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit():
    try:
        cursor = mysql.connection.cursor()
        reg = request.form['regNum']
        name = request.form['studentName']
        email = request.form['studentEmail']
        y1 = request.form['y1']
        y2 = request.form['y2']
        y3 = request.form['y3']
        if not reg or not name or not email or not y1 or not y2 or not y3:
            error_message = "Please fill in all the form fields."
            return render_template("failed.html", error_message=error_message)

        thesum = sum([int(y1), int(y2), int(y3)])
        print(thesum)
        percentage = (int(thesum) * 100)/300
        sql = "INSERT INTO students (reg_num, student_name, student_email, y1_marks, y2_marks, y3_marks, marks_percentage, marks_sum) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            reg, name, email, y1, y2, y3, int(percentage), int(thesum))
        cursor.execute(sql)
        cursor.connection.commit()
        with open('data.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([reg, name, email, y1, y2, y3])

        return render_template("success.html")
    except Exception as e:
        print(f"Error occurred: {e}")
        return redirect("/error")


@app.route('/data')
def get_data():
    try:
        cursor = mysql.connection.cursor()
        sqlget = "SELECT * FROM students"
        cursor.execute(sqlget)
        data = cursor.fetchall()
        cursor.close()
        return render_template("data.html", data=data)
    except Exception as e:
        error_message = "An error occurred. Please check the error log for more details. {e}"
        return render_template("failed.html", error_message=error_message)


if __name__ == "__main__":
    app.run()
