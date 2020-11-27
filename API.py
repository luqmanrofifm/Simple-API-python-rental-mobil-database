import flask
from flask import request, jsonify
from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MySQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root' #isi dengan user mu 
app.config['MYSQL_PASSWORD'] = 'luqmanklaten060800' #isi dengan passwordmu
app.config['MYSQL_DB'] = 'rental_mobil' #isi databasemu
app.config["DEBUG"] = True
mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/listcar', methods=['GET'])
def list_car():
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
    _json = request.json
    _car_id = _json['car_id']
    _car_name = _json['car_name']
    _car_type = _json['car_type']
    _hire_cost = _json['hire_cost']
    curPost = mysql.connection.cursor()
    query = "INSERT INTO daftar_mobil (car_id, car_name, car_type, hire_cost) VALUES (%d, %s, %s, %d)"
    data = (_car_id, _car_name, _car_type, _hire_cost)
    curPost.execute( query, data)
    mysql.commit()
    resp = jsonify('Car reservation added successfully!')
    return resp


app.run()