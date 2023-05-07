from flask import Flask, redirect

app = Flask(__name__)


@app.round('/login')
def login():
