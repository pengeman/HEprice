import logging
## 获得换热器各部件的信息，如果是单条记录返回entity,如果是多条记录，返回list(entity)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from DAO.DB import createDB
from entity.Flange1 import Flange1
from entity.Package import Package
from entity.Sheet import Sheet
from entity.SheetArea import SheetArea
from entity.Splint import Splint
from entity.Texture import Texture
from entity.Thinkness import Thinkness

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://peng:sa@127.0.0.1:3306/heat_exchanger'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
# db = SQLAlchemy(app)

db = createDB(app)

# 获得所有板型数据
def getSheetall():
    sheet_ls = list()
    with app.app_context():
        sql = text(" select id , type, pic from u_sheet ")
        list_sheet = db.session.execute(sql)
        for sheet in list_sheet:
            #print(str(sheet[0]) + " - " + sheet[1])
            sheet_entity = Sheet()
            sheet_entity.id = sheet[0]
            sheet_entity.type = sheet[1]
            sheet_entity.pic = sheet[2]
            sheet_ls.append(sheet_entity)
    return sheet_ls


# 获得板片数据by板型
def getSheetByType(type):
    sheet_entity = Sheet()
    with app.app_context():
        sql = text("select id , type , pic from u_sheet where type like '%%%%" + type + "%%%%'")
        #logging.debug(sql)
        list_sheet = db.session.execute(sql)
        sheet = list_sheet.fetchall()
        l = len(sheet)
        if l == 1:
            sheet_entity.id = sheet[0].id
            sheet_entity.type = sheet[0].type
            sheet_entity.pic = sheet[0].pic
            return sheet_entity
        else:
            if l == 0:
                msg = "没有查询到结果"
            else:
                msg = "查询的结果多余1条数据，请检查查询条件"
            return msg


# 得到板型单价
# 参数： 板型，材质， 厚度
# BP100B, 304, 0,5
def getPriceByType(sheet,texture, thinkness):
    with app.app_context():
        sql = text("select sheet_id , texture_id , thinkness_id, price , b.type, c.texture, d.thinkness "
                   "from u_price a inner join  u_sheet b on a.sheet_id = b.id inner join u_texture c on a.texture_id = c.id inner join  u_thinkness d on a.thinkness_id = d.id "
                   "where b.type = %s and c.texture = %s and d.thinkness = %s")
        params = (sheet, texture, thinkness)
        sheets = db.session.execute(sql, params)
        sheet_ls = sheets.fetchone()
        return sheet_ls[3]


# 获得夹板数据all select id,type,pressure,classmin,classmax lining price , pic from u_splint
def getSplintAll():
    with app.app_context():
        splint_ls = list()
        sql = text ("select id,type,pressure,classmin,classmax , lining ,price , pic from u_splint")
        spling_list = db.session.execute(sql)
        for splint in spling_list:
            splint_entity = Splint()
            splint_entity.id = splint[0]
            splint_entity.type = splint[1]
            splint_entity.pressure = splint[2]
            splint_entity.classmin = splint[3]
            splint_entity.classmax = splint[4]
            splint_entity.lining = splint[5]
            splint_entity.price = splint[6]
            splint_entity.pic = splint[7]
            splint_ls.append(splint_entity)
    return splint_ls



# 获得夹板数据by板型
def getSplingbyType(type,pressure,classnum,lining):
    with app.app_context():
        #splint_ls = list()
        splint_entity = Splint()
        sql = text ("select id,type,pressure,classmin,classmax , lining ,price , pic from u_splint where type like '%%%%" + type + "%%%%' and pressure = " + str(pressure) + " and lining = '" + str(lining) + "' and classmin < " + str(classnum) + "  and classmax >= " + str(classnum))
        spling_list = db.session.execute(sql)
        #splint_entity = Splint()
        splint_ls = spling_list.fetchall()
        l = len(splint_ls)
        if l == 1:
            splint_entity.id = splint_ls[0].id
            splint_entity.type = splint_ls[0].type
            splint_entity.pressure = splint_ls[0].pressure
            splint_entity.classmin = splint_ls[0].classmin
            splint_entity.classmax = splint_ls[0].classmax
            splint_entity.lining = splint_ls[0].lining
            splint_entity.price = splint_ls[0].price
            splint_entity.pic = splint_ls[0].pic
            return splint_entity
        else:
            if l == 0:
                msg = "没有查询到结果"
            else:
                msg = "查询的结果多余1条数据，请检查查询条件"
            return msg


# 获得板型单板面积数据all
def getSheetAreaAll():
    sql = text("select id,sheet,arear from u_sheetarea")
    with app.app_context():
        area_ls = list()
        area_list = db.session.execute(sql)
        #area_entity = SheetArea()
        for area in area_list:
            area_entiey = SheetArea()
            area_entiey.id = area[0]
            area_entiey.sheet = area[1]
            area_entiey.area = area[2]
            area_ls.append(area_entiey)
    return area_ls

# 获得单板面积by板型
def getSheetAreaByType(type):
    sql = text(" select id , sheet , arear from u_sheetarea where sheet like '%%%%" + type + "%%%%'")
    area_entity = SheetArea()
    area = db.session.execute(sql)
    area_ls = area.fetchall()
    l = len(area_ls)
    if l == 1:
        area_entity.id = area_ls[0].id
        area_entity.sheet = area_ls[0].sheet
        area_entity.area = area_ls[0].arear
        return area_entity
    else:
        if l == 0:
            msg = "没有查询到记录"
        if l > 1:
            msg = "查询的结果多余1条数据，请检查查询条件"
        return msg

# 获得材质数据all
def getTextureAll():
    sql = text("select id,texture,about from u_texture")
    texture_ls = list()
    #tls = list()
    with app.app_context():
        tls = db.session.execute(sql)
        for texture in tls:
            texture_entity = Texture()
            texture_entity.id = texture[0]
            texture_entity.texture = texture[1]
            texture_entity.about = texture[2]
            texture_ls.append(texture_entity)
    return texture_ls


# 获得板片厚度数据all
def getThinknessAll():
    sql = text("select id,thinkness,about from u_thinkness")
    thinkness_ls = list()
    with app.app_context():
        r = db.session.execute(sql)
        for thinkness in r:
            thinkness_entity = Thinkness()
            thinkness_entity.id = thinkness[0]
            thinkness_entity.thinkness = thinkness[1]
            thinkness_entity.about = thinkness[2]
            thinkness_ls.append(thinkness_entity)
    return thinkness_ls

# 获得接管数据all

# 获得板型价格all

# 获得板型价格by板型

# 获得法兰数据all（T20592-09化工）
def getFlange1All():
    sql = text("select id , type , texture , class , price from u_flange1")
    with app.app_context():
        r = db.session.execute(sql)
        flange1_ls = list()
        for flange1 in r:
            flange1_entity = Flange1()
            flange1_entity.id = flange1[0]
            flange1_entity.type = flange1[1]
            flange1_entity.texture = flange1[2]
            flange1_entity.class_ = flange1[3]
            flange1_entity.price = flange1[4]
            flange1_ls.append(flange1_entity)
    return flange1_ls

# 获得法兰数据（T20592-09化工）by 型号，规格，材质
def getFlange1ByType(sheet,classs,texture):
    sql = text("select id , type , texture, class, price from u_flange1 where type = %s and class = %s and texture = %s")
    para = (sheet , classs, texture)
    with app.app_context():
        r = db.session.execute(sql,para)
        flange1_ls  = r.fetchone()
        if flange1_ls is not None :
            flange1 = Flange1()
            flange1.id = flange1_ls[0]
            flange1.type = flange1_ls[1]
            flange1.texture = flange1_ls[2]
            flange1.class_ = flange1_ls[3]
            flange1.price = flange1_ls[4]
    return flange1

# 获得法兰数据all（T81-94国标）
def getFlange2All():
    sql = text("select id , type , texture , class , price from u_flange2")
    with app.app_context():
        r = db.session.execute(sql)
        flange2_ls = list()
        for flange1 in r:
            flange1_entity = Flange1()
            flange1_entity.id = flange1[0]
            flange1_entity.type = flange1[1]
            flange1_entity.texture = flange1[2]
            flange1_entity.class_ = flange1[3]
            flange1_entity.price = flange1[4]
            flange2_ls.append(flange1_entity)
    return flange2_ls

# 获得法兰数据（T81-94国标）by 型号，规格，材质
def getFlange2ByType(sheet,classs,texture):
    sql = text("select id , type , texture, class, price from u_flange2 where type = %s and class = %s and texture = %s")
    para = (sheet , classs, texture)
    with app.app_context():
        r = db.session.execute(sql,para)
        flange2_ls  = r.fetchone()
        if flange2_ls is not None :
            flange2 = Flange1()
            flange2.id = flange2_ls[0]
            flange2.type = flange2_ls[1]
            flange2.texture = flange2_ls[2]
            flange2.class_ = flange2_ls[3]
            flange2.price = flange2_ls[4]
    return flange2

# 获得包装数据all
def getPackageAll():
    sql = text("select     id, type, area, price     from u_package ")
    with app.app_context():
        r = db.session.execute(sql)
        package_ls = list()
        for packages in r:
            package_entity = Package()
            package_entity.id = packages[0]
            package_entity.type = packages[1]
            package_entity.area = packages[2]
            package_entity.price = packages[3]
            package_ls.append(package_entity)
    return package_ls


# 获得包装数据by型号，面积
def getPackageByType(sheet, area):
    sql = text("select     id, type, area, price     from u_package where type = %s and area = %s")
    para = (sheet , area)
    with app.app_context():
        r = db.session.execute(sql,para)
        packages = r.fetchone()
        if packages is not None:
            package_entity = Package()
            package_entity.id = packages[0]
            package_entity.type = packages[1]
            package_entity.area = packages[2]
            package_entity.price = packages[3]
    return package_entity


# 获得地托数据all

# 获得底托数据by型号


if __name__ == '__main__':
    #sheet_e = getSheetall()
    #for sheet in sheet_e:
    #    print("type - > " + sheet.type)
    ###################################
    # r = getSheetByType('BP100m')
    #
    # if isinstance(r,str):
    #     print(r)
    # if isinstance(r,Sheet):
    #     print(r.type)
    ##########################33
    # splints = getSplingAll()
    # for splint in splints:
    #     print("type - > " + splint.type + "-" + str(splint.pressure) + "-" + str(splint.lining) + "-" + str(splint.price))
    #################################
    # splints = getSplingbyType('BP100',16,50,'304')
    # if isinstance(splints,Splint):
    #     print(splints.type + "-" + str(splints.pressure)+ "-" + str(splints.lining) + "-" + str(splints.price))
    # if isinstance(splints,str):
    #     print(splints)
    ######################################
    # area_ls = getSheetAreaAll()
    # for area_entity in area_ls:
    #     print(area_entity.sheet + " - " + str(area_entity.area))
    ################################
    texture_ls = getTextureAll()
    for texture in texture_ls:
        print(str(texture.id) + " - " + texture.texture + " - " + str(texture.about))