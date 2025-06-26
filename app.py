# 这行代码会把所有 import MySQLdb 的调用，重定向到 pymysql，从而避免你没有安装 MySQLdb 的错误。
import pymysql

pymysql.install_as_MySQLdb()

import json
import logging.handlers
import re

from flask import Flask, redirect, render_template, request, session, url_for

import service.HEservice
from service import workhomeService
from service.HEcompute import calHE
from service.HEservice import getColletAll
from service.login import login_check

logger = logging.getLogger("my_loger")


def setLogging():
    LOG_FORMAT = "%(asctime)s - [%(levelname)s] - %(message)s"
    # logging.basicConfig(filename="test.log", level=logging.DEBUG, format=LOG_FORMAT)
    # logger = logging.getLogger("my_loger")
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
app.secret_key = '123456'


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
            print("登陆成功，开始工作 ")
            session['user'] = user
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
        user = session.get("user")
        if user is None: return render_template("/loginhome/login.html", title='登录')
        HEtype = request.values.get("ht")
        HEprice_values = {
            'price_guide': 'xx',
            'price_90': 'xx',
            'price_80': 'xx',
            'price_70': 'xx'
        }
        # 正则验证HEtype格式
        pattern = r'^BP(32|50|100|150|200|250|300|350|400|450|500|550)[bm]\D{1,3}-\d{1,3}-(304|316|tai|ni|mo|ha)-(0.5|0.6|0.7|0.8|1.0|1.2)-(0.10|0.16|0.20|0.25)Mpa-(epdm|nbr|fkm)-(304|316)-(tan|304|316)-(1|2)$'
        va = validate_string(pattern, HEtype)
        logger.debug(va)
        if va is True:
            HEprice_values = calHE(HEtype)  # 计算单价
            return HEprice_values
        else:
            return "换热器格式不正确,<br/>请参考：换热器型号BP200mhv-300-304-0.5-0.16Mpa-密封垫片-衬套材质-接管方式-1/2化工标准/供热标准<br/>BP100bhv-30-304-0.5-0.16Mpa-epdm-304-304-1"


## 获得换热器的基本数据，用于在页面显示
@app.route("/calculateHE/basedata")
def HEbasedata():
    # 获得基本数据
    sheetoption_ls = service.workhomeService.getsheet()
    textureoption_ls = service.workhomeService.getTexture()
    thinknessoption_ls = service.workhomeService.getThinkness()
    pressureoption_ls = service.workhomeService.getPressure()
    packageoption_ls = service.workhomeService.getPackage()
    epdmoption_ls = service.workhomeService.getEpdm()
    liningoption_ls = service.workhomeService.getLining()
    pipelineoption_ls = service.workhomeService.getPipeline()
    flangeoption_ls = service.workhomeService.getFlange()  ## 法兰标准

    ## sheet option
    sheetoptions = ""
    textureoptions = ""
    thinknessoptions = ""
    epdmoptions = ""
    liningoptions = ""
    pressureoptions = ""
    pipelineoptions = ""
    flangeoptions = ""

    for sheetoption in sheetoption_ls:
        sheetoptions = sheetoptions + sheetoption
    sheetoptions = "{\"sheet\":\"" + sheetoptions + "\"}"

    for textureoption in textureoption_ls:
        textureoptions = textureoptions + textureoption
    textureoptions = "{\"texture\":\"" + textureoptions + "\"}"

    for thinknessoption in thinknessoption_ls:
        thinknessoptions = thinknessoptions + thinknessoption
    thinknessoptions = "{\"thinkness\":\"" + thinknessoptions + "\"}"

    for epdmoption in epdmoption_ls:
        epdmoptions = epdmoptions + epdmoption
    epdmoptions = "{\"epdm\":\"" + epdmoptions + "\"}"

    for liningoption in liningoption_ls:
        liningoptions = liningoptions + liningoption
    liningoptions = "{\"lining\":\"" + liningoptions + "\"}"

    for pressureoption in pressureoption_ls:
        pressureoptions = pressureoptions + pressureoption
    pressureoptions = "{\"pressure\":\"" + pressureoptions + "\"}"

    for pipelineoption in pipelineoption_ls:
        pipelineoptions = pipelineoptions + pipelineoption
    pipelineoptions = "{\"pipeline\":\"" + pipelineoptions + "\"}"

    for flangeoption in flangeoption_ls:
        flangeoptions = flangeoptions + flangeoption
    flangeoptions = "{\"flange\":\"" + flangeoptions + "\"}"

    r = list()
    r.append(sheetoptions)
    r.append(textureoptions)
    r.append(thinknessoptions)
    r.append(epdmoptions)
    r.append(liningoptions)
    r.append(pressureoptions)
    r.append(pipelineoptions)
    r.append(flangeoptions)
    return r


# 打开页面，设置后台数据
@app.route("/setup")
def setup():
    user = session.get("user")
    if user is None:
        return render_template("/loginhome/login.html", title="登录")
    url = request.args.get("menu")
    if url is None:
        return render_template("setup/setup.html", title="设置")
    if url == "collet":
        ## 获得底托的数据
        collet_list = getColletAll()
        collet_ls = list()
        # collet_entity = Collet()
        collet_newjson = []
        for collet_entity in collet_list:
            collet_json = collet_entity.jsonformat()
            collet_newjson.append(collet_json)
        js = json.dumps(collet_newjson)
        print(js)
        return render_template("setup/collet.html", js=js)
    if url == "sheet":
        ## 设置板片
        sheet_list = service.HEservice.getSheetAll()
        sheet_newjson = []
        for sheet_entity in sheet_list:
            sheet_json = sheet_entity.jsonformat()
            sheet_newjson.append(sheet_json)
        js = json.dumps(sheet_newjson)
        return render_template("setup/sheet.html", js=js)
    if url == "sheetprice":
        ## 设置板片价格
        sheetprice_list = service.HEservice.getPriceAll()
        price_newjson = list()
        for price_content in sheetprice_list:
            id = price_content["id"]
            type = price_content["type"]
            texture_id = price_content["texture_id"]
            texture = price_content["texture"]
            thickness_id = price_content["thickness_id"]
            thickness = price_content["thickness"]
            price = price_content["price"]
            price_json = {
                "id": str(id),
                "type": type,
                "texture_id": texture_id,
                "texture": texture,
                "thickness_id": thickness_id,
                "thickness": str(thickness),
                "price": str(price)
            }
            price_newjson.append(price_json)
            print(price_newjson)
        js = json.dumps(price_newjson)
        return render_template("setup/sheetprice.html", js=js)
    if url == "sheetarea":
        ## 设置板片面积
        sheetarea_list = service.HEservice.getSheetAreaAll()
        sheetarea_newjson = list()
        for sheetarea_entity in sheetarea_list:
            id = sheetarea_entity.id
            sheet = sheetarea_entity.sheet
            area = sheetarea_entity.area
            sheetarea_json = {
                "id": str(id),
                "sheet": sheet,
                "area": str(area)
            }
            sheetarea_newjson.append(sheetarea_json)
        js = json.dumps(sheetarea_newjson)
        return render_template("setup/sheetarea.html", js=js)
    if url == "splint":
        ## 设置夹板数据
        splint_list = service.HEservice.getsplintAll()
        splint_newjson = list()
        for splint_entity in splint_list:
            id = splint_entity.id
            type = splint_entity.type
            classmin = splint_entity.classmin
            classmax = splint_entity.classmax
            pressure = splint_entity.pressure
            lining = splint_entity.lining
            price = splint_entity.price
            splint_json = {
                "id": str(id),
                "pressure": str(pressure),
                "classmin": str(classmin),
                "classmax": str(classmax),
                "lining": str(lining),
                "price": str(price)
            }
            splint_newjson.append(splint_json)
        js = json.dumps(splint_newjson)
        return render_template("setup/splint.html", js = js)


    return "你来干什么，你看到什么了？小心我灭口"


@app.route("/setup/sheet")
def getsheets():
    ## 得到板片信息
    sheet_ls = list()
    r = service.HEservice.getSheetAll()
    for sheet_entity in r:
        id = sheet_entity.id
        type = sheet_entity.type
        sheet_dict = {
            "id": str(id), "type": type
        }
        sheet_ls.append(sheet_dict)
    sheet_js = json.dumps(sheet_ls)
    return sheet_js


@app.route("/setup/texture")
def gettexture():
    ## 得到材质信息
    texture_ls = list()
    r = service.HEservice.getTextureAll()
    for texture_entity in r:
        id = texture_entity.id
        texture = texture_entity.texture
        texture_dict = {
            "id": str(id), "texture": texture
        }
        texture_ls.append(texture_dict)
    texture_js = json.dumps(texture_ls)
    return texture_js


@app.route("/setup/thickness")
def getthickness():
    ## 得到厚度信息
    thickness_ls = list()
    r = service.HEservice.getThinknessAll()
    for thickness_entity in r:
        id = thickness_entity.id
        thickness = thickness_entity.thinkness
        thickness_dict = {
            "id": str(id), "thickness": str(thickness)
        }
        thickness_ls.append(thickness_dict)
    thickness_js = json.dumps(thickness_ls)
    return thickness_js


@app.route("/setup/newcollet")
def newcollet():
    type = request.args.get("type")
    price = request.args.get("price")
    r = service.HEservice.newCollet(type, price)  ## 如果执行成功返回1,否则返回0
    print(r)
    return str(r)


@app.route("/setup/updatecollet")
def updatecollet():
    id = request.args.get("id")
    type = request.args.get("type")
    price = request.args.get("price")
    r = service.HEservice.updateCollet(id, type, price)  ## 如果执行成功返回1,否则返回0
    print(r)
    return str(r)


@app.route("/setup/newsheetprice")
def newsheetprice():
    type = request.args.get("type")
    texture = request.args.get("texture")
    thickness = request.args.get("thickness")
    price = request.args.get("price")
    r = service.HEservice.newsheetprice(type, texture, thickness, price)
    if r == 1:
        msg = "新增一条板片价格成功"
    else:
        msg = "新增一条板片价格失败"
    return msg

@app.route("/setup/updatesheetprice")
def updatesheetprice():
    type = request.args.get("type")
    texture = request.args.get("texture")
    thickness = request.args.get("thickness")
    price = request.args.get("price")
    r = service.HEservice.updatesheetprice(type,texture,thickness,price)
    if r == 1:
        msg = "更新板片价格成功"
    else:
        msg = "更新板片价格失败"
    return msg


@app.route("/setup/newsheet")
def newsheet():
    type = request.args.get("type")
    r = service.HEservice.newsheet(type)
    if r == 1:
        msg = "新增一条板片数据成功"
    else:
        msg = "新增一条板片数据失败"
    return msg

@app.route("/setup/updatesheet")
def updatesheet():
    type = request.args.get("type")
    id = request.args.get("id")
    r = service.HEservice.updatesheet(id, type)
    if r == 1:
        msg = "更新板片数据成功"
    else:
        msg = "更新板片价数据败"
    return msg

@app.route("/setup/newsheetarea")
def newsheetarea():
    sheet = request.args.get("type")
    area = request.args.get("area")
    r = service.HEservice.newsheetarea(sheet, area)
    if r == 1:
        msg = "新增板片数据面积数据成功"
    else:
        msg = "新增板片数据失败面积数据"
    return msg

@app.route("/setup/updatesheetarea")
def updatesheetarea():
    area = request.args.get("area")
    type = request.args.get("type")
    id = request.args.get("id")
    r = service.HEservice.updatesheetarea(id, type,area)
    if r == 1:
        msg = "更新板片面积成功"
    else:
        msg = "更新板片面积失败"
    return msg

@app.route("/setup/newsplint")
def newsplint():
    return None

def validate_string(pattern, input_string):
    # pattern = r'^BP(32|50|100|150|200|250|300|350|400|450|500|550)[bm]\d{1,3}-[304|316|tai|ni|mo|ha]-[0.5|0.6|0.7|0.8|1.0|1.2]-\d{0.1|0.16|0.2|0.25}Mpa-[epdm|nbr|fkm]-(304|316)衬套-[tan|304|316]接管-(1|2)$'

    if re.match(pattern, input_string):
        print("字符串验证通过")
        return True
    else:
        print("字符串验证失败")
        return False


if __name__ == '__main__':
    app.run(port=9999)
