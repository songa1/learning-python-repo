#!/usr/bin/python3

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'webapp_db'

mysql = MySQL(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
	regNum = request.form['regNum']
	studentName = request.form['studentName']
	userEmail = request.form['studentEmail']
	y1 = request.form['y1']
	y2 = request.form['y2']
	y3 = request.form['y3']
	thesum = sum([int(y1), int(y2), int(y3)]);
	print(thesum)

	percentage = (int(thesum) * 100)/300;
	cursor = mysql.connection.cursor()
	sql = "INSERT INTO students (reg_num, student_name, student_email, y1_marks, y2_marks, y3_marks, marks_percentage, marks_sum) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(regNum, studentName, userEmail, y1, y2, y3,int(percentage), int(thesum))
	cursor.execute(sql)
	cursor.connection.commit()	
	return f"Student Inserted"

if __name__ == "__main__":
	app.run()
