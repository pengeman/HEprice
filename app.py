from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return redirect('/login')


@app.route('/index')
def index():
    return redirect("/login")


if __name__ == '__main__':
    app.run()
