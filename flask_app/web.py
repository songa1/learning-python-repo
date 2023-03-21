#!/usr/bin/python3

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'web_app_py'

mysql = MySQL(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
	regNum = request.form['regNum']
	studentName = request.form['studentName']
	userEmail = request.form['userEmail']
	userSchool = request.form['userSchool']
	cursor = mysql.connection.cursor()
	sql = "INSERT INTO students (reg_num, student_name, user_email, user_school) VALUES ('{}', '{}', '{}', '{}')".format(regNum, studentName, userEmail, userSchool)
	cursor.execute(sql)
	cursor.connection.commit()	
	return f"Student Inserted"

if __name__ == "__main__":
	app.run()
