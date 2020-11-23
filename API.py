import flask
from flask import request, jsonify
from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MySQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root' #isi dengan user mu 
app.config['MYSQL_PASSWORD'] = '###### ' #isi dengan passwordmu
app.config['MYSQL_DB'] = 'rental_mobil'
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
    #cur.close()
#    return '''<h1>Distant Reading Archive</h1>
#<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
#@app.route('/api/v1/resources/books/all', methods=['GET'])
#def api_all():
#    return jsonify(books)
def createReservation():
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO coba (name, class, description) VALUES (%s, %s, %s)")


app.run()