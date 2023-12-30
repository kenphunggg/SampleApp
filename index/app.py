from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__, template_folder = "templates")

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        cnx = mysql.connector.connect(user = 'root', password = f'{os.getenv("MYSQL_ROOT_PASSWORD")}', host = f'{os.getenv("MYSQL_SERVICE")}', database = 'sampleapp2', port='3306')
        cursor = cnx.cursor()
        username = request.form["username"]
        password = request.form["password"]
        cursor.execute(f"SELECT username FROM form WHERE username = '{username}' AND password = '{password}';")
        found = cursor.fetchone()
        if found:
            return requests.get(f'{os.getenv("FORWARD_PYTHON")}').content
            #return 'hiken'
        else:
            return render_template('index.html')
        cursor.close()
        cnx.close()
    return render_template('index.html')
    
@app.route('/forward')
def forward():
    return 'hi ken'

if __name__ == '__main__':
    app.run(debug = True)
