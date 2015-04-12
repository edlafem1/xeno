import mysql.connector
from mysql.connector import MySQLConnection, Error
from flask import g

@app.before_request
def connect_db():
    db = mysql.connector.Connect(host='localhost',user='root',password='',database='mysql')
    g.db = db.cursor()

@app.after_request
def release_db():
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()