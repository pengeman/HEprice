### 提供换热器的相关数据
import DAO.HEdao

# 获得sheet的全部数据
def getSheetAll():
    sheet_list = DAO.HEdao.getSheetall()
    return  sheet_list

def getTextureAll():
    texture_list = DAO.HEdao.getTextureAll()
    return texture_list

def getThinknessAll():
    return DAO.HEdao.getThinknessAll()

## 得到承压的数据
def getPressureAll():
    return  DAO.HEdao.getPressureAll()

## 得到垫片的数据
def getEpdmAll():
    return DAO.HEdao.getEpdmAll()

## 得到衬套材质数据
def getLiningAll():
    return DAO.HEdao.getLiningAll()

## 得到接管材质数据
def getPipelingAll():
    return  DAO.HEdao.getPipelineAll()

## 得到法兰标准数据
def getFlangeAll():
    return DAO.HEdao.getFlangeSTDAll()

## 得到板片价格
def getPriceAll():
    return DAO.HEdao.getPriceAll()

def getPackageAll():
    return DAO.HEdao.getPackageAll()

# 获得底托的全部数据
# return list(entity)
def getColletAll():
    collet_ls = DAO.HEdao.getColletAll()
    return collet_ls

def getSheetAreaAll():
    return DAO.HEdao.getSheetAreaAll()

# 新增一个底托价格
# 参数：板型，单价
# 返回：0失败，1成功
def newCollet(type, price):
    r = DAO.HEdao.newCollet(type, price)
    if r > 0:
        return 1
    else:
        return 0


# 更新一个底托价格
# 参数：板型，单价
# 返回：0失败，1成功
def updateCollet(id, type, price):
    r = DAO.HEdao.updateCollet(id,type, price)
    if r > 0:
        return 1
    else:
        return 0


## 新增一个板片价格
def newsheetprice(sheet, texture, thickness, price):
    r = DAO.HEdao.newsheetprice(sheet,texture,thickness,price)
    return r


## 更新一个板片价格
def updatesheetprice(type, texture, thickness, price):
    r = DAO.HEdao.updateshetprice(type,texture,thickness,price)
    return r

## 新曾一个板片数据
def newsheet(type):
    r = DAO.HEdao.newSheet(type)
    return r


def updatesheet(id, type):
    r = DAO.HEdao.updatesheet(id,type)
    return r


def newsheetarea(sheet, area):
    r = DAO.HEdao.newsheetArea(sheet, area)
    return r


def updatesheetarea(id, type, area):
    r = DAO.HEdao.updatesheetarea(id,type,area)
    return r