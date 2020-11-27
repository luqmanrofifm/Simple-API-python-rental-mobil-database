# Prerequisites: Python 2.7, Flask 0.12.2, Python-Mysql connector
# sudo pip install Flask
# sudo apt install python-mysqldb
# sudo pip install -U flask-cors

# Run with:
# FLASK_APP=hello.py flask run

# http://flask.pocoo.org/docs/0.12/api/#flask.request
from flask import Flask,request

# https://pypi.python.org/pypi/Flask-Cors
#from flask_cors import CORS, cross_origin

# https://pythonspot.com/mysql-with-python/
import MySQLdb
import json

app = Flask(__name__)
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, methods=['GET', 'POST', 'DELETE', 'PUT'])


@app.route("/api/v1/listcar",methods=['GET'])
def getStudents():

    db = MySQLdb.connect(host="localhost",  # your host 
                         user="root",       # username
                         passwd="luqmanklaten060800",     # password
                         db="rental_mobil")   # name of the database

    # Create a Cursor object to execute queries.
    cur = db.cursor()

    # Select data from table using SQL query.
    cur.execute("SELECT * FROM daftar_mobil")

    rows = cur.fetchall()
    row_headers=[x[0] for x in cur.description] #this will extract row headers

    json_data=[]
    for result in rows:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)

@app.route("/api/v1/carreservation",methods=['POST'])
def createStudent():
    requestData = request.get_json()

    db = MySQLdb.connect(host="localhost",  # your host 
                         user="root",       # username
                         passwd="luqmanklaten060800",     # password
                         db="rental_mobil")   # name of the database

    # Create a Cursor object to execute queries.
    cur = db.cursor()

    # https://stackoverflow.com/questions/7929364/python-best-practice-and-securest-to-connect-to-mysql-and-execute-queries
    # Select data from table using SQL query.
    cur.execute("INSERT INTO daftar_mobil (car_id, car_name, car_type, hire_cost) VALUES (%d, %s, %s, %d)", (requestData["car_id"],requestData["car_name"],requestData["car_type"],requestData["hire_cost"]))
    db.commit()

    return "OK"

'''
@app.route("/api/v1/students",methods=['PUT'])
def updateStudents():
    requestData = request.get_json()

    db = MySQLdb.connect(host="localhost",  # your host 
                         user="root",       # username
                         passwd="password",     # password
                         db="rental_mobil")   # name of the database

    # Create a Cursor object to execute queries.
    cur = db.cursor()

    # https://stackoverflow.com/questions/7929364/python-best-practice-and-securest-to-connect-to-mysql-and-execute-queries
    # Select data from table using SQL query.
    cur.execute("UPDATE students SET name=%s, class=%s, town=%s, roll=%s WHERE id=%s", (requestData["name"],requestData["class"],requestData["town"],requestData["roll"],requestData["id"]))
    db.commit()

    return "OK"

@app.route("/api/v1/students/<int:student_id>",methods=['DELETE'])
def deleteStudent(student_id):
    requestData = request.get_json()

    db = MySQLdb.connect(host="localhost",  # your host 
                         user="root",       # username
                         passwd="password",     # password
                         db="pythontesting")   # name of the database

    # Create a Cursor object to execute queries.
    cur = db.cursor()

    # Select data from table using SQL query.
    cur.execute("DELETE FROM students WHERE id=%s", (student_id,))
    db.commit()

    return "OK"
'''
app.run()