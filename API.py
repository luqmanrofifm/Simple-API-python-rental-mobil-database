import flask
import mysql.connector
from flask import request, jsonify
from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/listcar', methods=['GET'])
def list_car():
    try:
        db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="luqmanklaten060800",
                                     database="rental_mobil"
                                    )
        cur = db.cursor()
        cur.execute("SELECT * FROM daftar_mobil")
        row_headers=[x[0] for x in cur.description]
        rv = cur.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return jsonify(json_data)
    except Exception as e:
        print(e)
    finally:
        cur.close() 
        db.close()

@app.route('/reservemobil', methods=['POST'])
def createReservation():   
    try:
        _json = request.form
        carID = request.form['car_id']
        carName = request.form['car_name']
        carType = request.form['car_type']
        hireCost = request.form['hire_cost']		
        if carID and carName and carType and hireCost and request.method == 'POST':			
            sqlQuery = "INSERT INTO daftar_mobil(car_id, car_name, car_type, hire_cost) VALUES(%s, %s, %s, %s)"
            bindData = (carID, carName, carType, hireCost)
            db = mysql.connector.connect(host="localhost",
                                         user="root",
                                         passwd="luqmanklaten060800",
                                         database="rental_mobil"
                                        )
            cursor = db.cursor()
            cursor.execute(sqlQuery, bindData)
            db.commit()
            respone = jsonify('Employee added successfully!')
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        db.close()

app.run()