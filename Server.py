import sqlite3
import shutil
import os

from flask import Flask, render_template, redirect, request,send_file
from werkzeug.utils import secure_filename
app = Flask(__name__)

path = os.getcwd()
# UPLOAD_FOLDER = os.path.join(path, 'static/uploads')

# if not os.path.isdir(UPLOAD_FOLDER):
#     os.mkdir(UPLOAD_FOLDER)

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        # cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname TEXT NOT NULL, lastname TEXT NOT NULL, email TEXT NOT NULL, contact_no TEXT NOT NULL, account_type TEXT NOT NULL)')
        conn.commit()
    return render_template('home.html')

@app.route('/map', methods=['GET'])
def direct_map():
    return render_template("map.html")

@app.route('/data', methods=['GET'])
def direct_data():
    return render_template("data.html")

 
if __name__ == '__main__':
    app.run(debug=True)
