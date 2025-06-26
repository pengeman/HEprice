## 获得flask_sqlalchemy 的db对象

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from entity.Sheet import Sheet
from entity.SheetArea import SheetArea
from entity.Splint import Splint
from entity.Texture import Texture
from entity.Thinkness import Thinkness


def createDB(n):
    app = n

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://peng:peng@127.0.0.1:3306/heat_exchanger'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db = SQLAlchemy(app)
    return db
