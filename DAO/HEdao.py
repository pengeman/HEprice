from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://peng:sa@127.0.0.1:3306/heat_exchanger'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
# 获得所有板型数据
def getSheetall():
    sql = " select id , type, pic from u_sheet "
    list_sheet = db.session.execute(sql)
    for sheet in list_sheet:
        print(sheet[0] + " - " + sheet[1])

# 获得板片数据by板型

# 获得夹板数据all

# 获得夹板数据by板型

# 获得板型单板面积数据all

# 获得材质数据all

# 获得板片厚度数据all

# 获得接管数据all


if __name__ == '__main__':
    getSheetall()

#
