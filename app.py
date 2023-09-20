import sqlite3
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import psycopg2





app = Flask(__name__)


@app.route('/')
def index():
   
    conn = psycopg2.connect(database="new_db",
                            user="postgres",
                            password="Ubiquo.12",
                            host="localhost", port="5434")
  
    # create a cursor
    cur = conn.cursor()

    # Select all products from the table
    cur.execute('''SELECT * FROM song''')

    # Fetch the data
    data = cur.fetchall()

    # close the cursor and connection
    cur.close()
    conn.close()

    return render_template('index.html', data=data)

@app.route('/result')
def result():
   
    conn = psycopg2.connect(database="new_db",
                            user="postgres",
                            password="Ubiquo.12",
                            host="localhost", port="5434")
  
    # create a cursor
    cur = conn.cursor()

    # Select all products from the table
    cur.execute('''SELECT * FROM artist''')

    # Fetch the data
    data = cur.fetchall()

    # close the cursor and connection
    cur.close()
    conn.close()

    return render_template('result.html', data=data)



if __name__ == '__main__':
    app.run(debug=True)


