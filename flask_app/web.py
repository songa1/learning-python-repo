#!/usr/bin/python3

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask_db'

mysql = MySQL(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
	regNum = request.form['regNum']
	studentName = request.form['studentName']
	userEmail = request.form['userEmail']
	y1 = request.form['y1']
	y2 = request.form['y2']
	y3 = request.form['y3']
	markSum = int(y1 + y2 + y3)
	markAverage = markSum/3
	percentage = (markSum * 100) / 300
	cursor = mysql.connection.cursor()
	sql = "INSERT INTO flask (reg_num, student_name, user_email, y1, y2, y3, sum, average, percentage) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(regNum, studentName, userEmail, y1, y2, y3, markSum, markAverage, percentage)
	cursor.execute(sql)
	cursor.connection.commit()	
	return render_template("success.html")

@app.route('/data')
def getData():

	return render_template("data.html")

if __name__ == "__main__":
	app.run()
