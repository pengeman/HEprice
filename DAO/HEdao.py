import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from entity.Sheet import Sheet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://peng:sa@127.0.0.1:3306/heat_exchanger'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
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

if __name__ == '__main__':
    sheet_e = getSheetall()
    for sheet in sheet_e:
        print("type - > " + sheet.type)

# 获得板片数据by板型
def getSheetByType(type):
    sheet_entity = Sheet()
    with app.app_context():
        sql = text("select id , type , pic from u_sheet where type = '" + type + "'")
        logging.debug(sql)
        list_sheet = db.session.execute(sql)
        if len(list_sheet) == 1:
            sheet_entity.id = list_sheet[0]
            sheet_entity.type = list_sheet[1]
            sheet_entity.pic = list_sheet[2]
            return sheet_entity
        else:
            return 0

# 获得夹板数据all

# 获得夹板数据by板型

# 获得板型单板面积数据all

# 获得材质数据all

# 获得板片厚度数据all

# 获得接管数据all



#
