from flask import Flask, redirect, url_for, render_template, request

from controllers.loginhome import login
from service.HEcompute import calHE
from service.login import login_check
import logging.handlers

def setLogging():
    LOG_FORMAT = "%(asctime)s - [%(levelname)s] - %(message)s"
    # logging.basicConfig(filename="test.log", level=logging.DEBUG, format=LOG_FORMAT)
    logger = logging.getLogger("my_loger")
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    log_format = logging.Formatter(LOG_FORMAT)

    console_handler.setFormatter(log_format)

    file_handler = logging.FileHandler("my_test.log", encoding="utf-8")

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    #logger.debug("this is debug log")
    #logger.info("this is info log")


def create_app():
    app = Flask(__name__, template_folder='./templates', static_folder='./static')
    #app.config.from_object(settings)
    #app.register_blueprint(login)
    setLogging()
    return app


loginhomepage = "loginhome/login.html"
workhomepage = "HEcalculate/HEhome.html"
app = create_app()


@app.route('/')
def home():  # put application's code here
    return render_template(loginhomepage, title='kdkd')


@app.route('/login',methods=['POST'])
def login():
    isok = 0
    print("login...............")
    if request.method == 'POST':  # 请求方式是post
        message = "用户名和密码错误"
        user = request.args.get('username')  # args取get方式参数
        pwd = request.args.get('password')
        ## 验证用户名和密码
        isok = login_check(user,pwd)
        if isok:
            print("isok : " + str(isok))
            return render_template(workhomepage)
        else:
            return render_template(loginhomepage, message=message)
    else:
        return render_template(loginhomepage);

@app.route("/login2",methods=['POST'])
def login2():
    return render_template("HEcalculate/HEhome.html")

@app.route('/index')
def index():
    print("index......")
    return redirect("/")





@app.route('/calculateHE',methods=['POST'])
def calculateHE(HEtype):  # 计算换热器单价(换热器型号BP200mhv-300-304/0.5-0.16Mpa-密封垫片-接管方式)
    HEprice_values = {
        'price_guide' : 'xx',
        'price_90' : 'xx',
        'price_80' : 'xx',
        'price_70' : 'xx'
    }
    calHE(HEtype) # 计算单价





if __name__ == '__main__':
    app.run()

