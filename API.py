import flask
from flask import request, jsonify
from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MySQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root' #isi dengan user mu 
app.config['MYSQL_PASSWORD'] = '######' #isi dengan passwordmu
app.config['MYSQL_DB'] = 'rental_mobil' #isi databasemu
app.config["DEBUG"] = True
mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM daftar_mobil")
    row_headers=[x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)

@app.route('/reservemobil', methods=['POST'])
def createReservation():
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO daftar_mobil (car_id, car_name, car_type, hire_cost) VALUES (%d, %s, %s, %d)")
    mysql.commit()
    return "Reserved"


app.run()