from flask import Flask, redirect, url_for, render_template

from controllers.loginhome import login
from service.login import login_check


def create_app():
    app = Flask(__name__, template_folder='./templates', static_folder='./static')
    #app.config.from_object(settings)
    #app.register_blueprint(login)
    return app


app = create_app()



@app.route('/')
def home():  # put application's code here
    return render_template("loginhome/login.html",title='kdkd')


@app.route('/login',methods=['POST'])
def login():
    login_check()

@app.route('/index')
def index():
    print("index......")
    return redirect("/vccvvc")



if __name__ == '__main__':
    app.run()

