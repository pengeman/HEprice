from flask import Flask, redirect, url_for, render_template, request
from regex import regex
import re
from controllers.loginhome import login
from service.HEcompute import calHE
from service.login import login_check
import logging.handlers

logger = logging.getLogger("my_loger")
def setLogging():
    LOG_FORMAT = "%(asctime)s - [%(levelname)s] - %(message)s"
    # logging.basicConfig(filename="test.log", level=logging.DEBUG, format=LOG_FORMAT)
    #logger = logging.getLogger("my_loger")
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    log_format = logging.Formatter(LOG_FORMAT)

    console_handler.setFormatter(log_format)

    file_handler = logging.FileHandler("my_test.log", encoding="utf-8")

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.debug("this is debug log")
    logger.info("this is info log")


def create_app():
    app = Flask(__name__, template_folder='./templates', static_folder='./static')
    # app.config.from_object(settings)
    # app.register_blueprint(login)
    setLogging()
    return app


loginhomepage = "loginhome/login.html"
workhomepage = "HEcalculate/HEhome.html"
app = create_app()


@app.route('/')
def home():  # put application's code here
    return render_template(loginhomepage, title='kdkd')


@app.route('/login', methods=['POST'])
def login():
    isok = 0
    print("login...............")
    if request.method == 'POST':  # 请求方式是post
        message = "用户名和密码错误"
        user = request.form.get('username')  # args取get方式参数
        pwd = request.form.get('password')
        ## 验证用户名和密码
        isok = login_check(user, pwd)
        if isok:
            print("app.py59 : " + str(isok))
            return render_template(workhomepage)
        else:
            return render_template(loginhomepage, message=message)
    else:
        return render_template(loginhomepage);


@app.route('/index')
def index():
    print("index......")
    return redirect("/")


@app.route('/calculateHE', methods=['POST'])
def calculateHE():  # 计算换热器单价(换热器型号BP200mhv-300-304/0.5-0.16Mpa-密封垫片-接管方式)
    if request.method == "POST":
        HEtype = request.values.get("ht")
        HEprice_values = {
            'price_guide': 'xx',
            'price_90': 'xx',
            'price_80': 'xx',
            'price_70': 'xx'
        }
        # 正则验证HEtype格式
        pattern = r'^BP(32|50|100|150|200|250|300|350|400|450|500|550)[bm]\D{1,3}-\d{1,3}-(304|316|tai|ni|mo|ha)-(0.5|0.6|0.7|0.8|1.0|1.2)-(0.1|0.16|0.2|0.25)Mpa-(epdm|nbr|fkm)-(304|316)衬套-(tan|304|316)接管-(1|2)$'
        va = validate_string(pattern, HEtype)
        logger.debug(va)
        if va is True:
            calHE(HEtype)  # 计算单价
            return "HEprice_values"
        else:
            return "换热器格式不正确"



def validate_string(pattern, input_string):
    # pattern = r'^BP(32|50|100|150|200|250|300|350|400|450|500|550)[bm]\d{1,3}-[304|316|tai|ni|mo|ha]-[0.5|0.6|0.7|0.8|1.0|1.2]-\d{0.1|0.16|0.2|0.25}Mpa-[epdm|nbr|fkm]-(304|316)衬套-[tan|304|316]接管-(1|2)$'

    if re.match(pattern, input_string):
        print("字符串验证通过")
        return True
    else:
        print("字符串验证失败")
        return False


if __name__ == '__main__':
    app.run()
