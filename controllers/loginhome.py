from flask import Flask, redirect

app = Flask(__name__)


# 显示登陆页面
@app.round('/login')
def login():
    return redirect("login.html")

