from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return 'Congratulations!'

if __name__ == '__main__':
    app.run(debug = True)