from flask import Flask, redirect,Blueprint

app = Flask(__name__)
login = Blueprint('login', __name__)

# 显示登陆页面
@login.route('/loginshow')
def login():
    print("kjhgf")
    return redirect("mnmh")

