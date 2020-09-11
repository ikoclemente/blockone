#-------------------------------------------------------------------------------
# Name:        enroll.py
# Purpose:     Flask based RESTful API
#
# Author:      FClemen
#
# Created:     05/09/2020
# Copyright:   (c) FClemen 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import flask
from flask import request, jsonify
from flask import render_template
import sqlite3
import traceback

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
   d = {}
   for idx, col in enumerate(cursor.description):
      d[col[0]] = row[idx]
   return d


@app.route('/', methods=['GET'])
def home():
   if request.form:
      print request.form
   return render_template("home.html")


@app.route('/fetchStudents/all', methods=['GET'])
def api_all():
   conn = sqlite3.connect('students.db')
   conn.row_factory = dict_factory
   cur = conn.cursor()
   all_students = cur.execute('SELECT * FROM students;').fetchall()

   return jsonify(all_students)

@app.errorhandler(404)
def page_not_found(e):
   return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/fetchStudents', methods=['GET'])
def api_filter():
   """ API filter based on id and class

   -- Example filters --
   http://127.0.0.1:5000//fetchStudents/all
   http://127.0.0.1:5000/fetchStudents?id=223445
   http://localhost:5000/fetchStudents?class=3 A
   """

   query_parameters = request.args

   id = query_parameters.get('id')
   _class = query_parameters.get('class')

   query = "SELECT * FROM students WHERE"
   to_filter = []

   if id:
      query += ' id=? AND'
      to_filter.append(id)
   if _class:
      query += ' class=? AND'
      to_filter.append(_class)

   if not (id or _class):
     return page_not_found(404)

   query = query[:-4] + ';'

   conn = sqlite3.connect('students.db')
   conn.row_factory = dict_factory
   cur = conn.cursor()

   results = cur.execute(query, to_filter).fetchall()

   return jsonify(results)


@app.route("/", methods = ["POST"])
def add_new_record():
   """ Add new record to students.db"""
   rec = {
         "id":223445,
         "firstName": "Mike",
         "lastName": "Wong",
         "class":"3 A",
         "nationality": "Singapore"
         }

   id = rec.get('id')
   firstname = rec.get('firstName')
   lastname = rec.get('lastName')
   _class = rec.get('class')
   nationality = rec.get('nationality')

   sql = "INSERT INTO students VALUES(%s, '%s', '%s', '%s', '%s')"%(id,firstname,lastname,_class,nationality)

   try:
      conn = sqlite3.connect('students.db')
      cur = conn.cursor()

      cur.execute(sql)
      conn.commit()
   except:
      print traceback.format_exec()
   finally:
      cur.close()
      conn.close()
      return render_template("home.html")


@app.route("/update", methods=["POST"])
def update():
   """ Update class based on record id """
   id = 223445
   new_class = '3 C'

   try:
      conn = sqlite3.connect('students.db')
      cur = conn.cursor()
      sql = "UPDATE students SET class = '%s' WHERE id = %s" %(new_class, id)

      cur.execute(sql)
      conn.commit()
   except:
      print traceback.format_exc()
   finally:
      cur.close()
      conn.close()

      return render_template("home.html")

@app.route("/delete", methods=["POST"])
def delete():
   """ Delete record ID from database """
   id = 223445

   try:
      conn = sqlite3.connect('students.db')
      cur = conn.cursor()
      sql = "DELETE from students where id = %s" %id

      cur.execute(sql)
      conn.commit()
   except:
      print traceback.format_exc()

   finally:
      cur.close()
      conn.close()
      return render_template("home.html")


app.run()