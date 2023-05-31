## 真逗user的操作

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from DAO.DB import createDB
from entity.Sheet import Sheet
from entity.SheetArea import SheetArea
from entity.Splint import Splint
from entity.Texture import Texture
from entity.Thinkness import Thinkness
from entity.User import User

app = Flask(__name__)

db = createDB(app)


class UserDao(object):

    def __init__(self):
        pass

    def getUserAll(self):
        sql = text("select id , name , code , password, deparment, role from u_user ")
        userlist = list()
        with app.app_context():
            r = db.session.execute(sql)
            for users in r:
                user = User();
                user.id = users[0]
                user.name = user[1]
                user.code = user[2]
                user.password = user[3]
                user.department = user[4]
                user.role = user[5]
                userlist.append(user)
        return userlist

    def getUserByName(self, name):
        sql = text(" select id , name , code , password , department, role from u_user where name = '" + str(name) + "'")
        with app.app_context():
            r = db.session.execute(sql)
            users = r.fetchone()
            if users is not None:
                user = User()
                user.id = users[0]
                user.name = users[1]
                user.code = users[2]
                user.password = users[3]
                user.department = users[4]
                user.role = users[5]
                return user
            else:
                return None


    def getUserById(self, id):
        sql = text(" select id , name , code , password , deparment, role from u_user where id = '" + str(id) + "'")
        with app.app_context():
            r = db.session.execute(sql)
            users = r.fetchone()
            if users is not None:
                user = User()
                user.id = users[0]
                user.name = users[1]
                user.code = users[2]
                user.password = users[3]
                user.department = users[4]
                user.role = users[5]
                return user
            else:
                return None
